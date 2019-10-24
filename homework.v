module test_ADDA(
	input clk,
	//DA PINS
	
	output reg [13:0]DA_A,
	output reg [13:0]DA_B,
	output DA_CLK_A,
	output DA_CLK_B,
	output DA_WR_A,
	output DA_WR_B,
	output reg[2:0] led,
	//AD PINS
	/*
	output AD_ECODE_A,
	output AD_ECODE_B,
	output AD_S1,
	output AD_S2,
	output AD_DFS_GAIN,
	*/
	input key,
	// input [9:0]AD_A,//使用AD9288时低2位无效
	// input [9:0]AD_B//使用AD9288时低2位无效
	input rxf,
	input txe,
	output reg wr,
	output reg rd,
	inout [7:0]d,
	output reg SI
);
	
	wire clk_40M;
	wire clk_125M;
	reg [4:0]state;
	reg [7:0]buffer;
	reg [7:0]dout;
	reg div_clk;
	reg div_clk2;

initial begin
		state <= 0;
		wr <= 0;
		rd <= 1;
		SI <= 1;
	end

	always @(posedge clk)
	begin	
		div_clk <= ~div_clk;
	end
	always @(posedge div_clk)
	begin	
		div_clk2 <= ~div_clk2;
	end	
	always @(posedge div_clk2)
	begin
		case(state)
			5'd0:   begin
						if(rxf == 0)begin
							rd <= 0;
							state <= 1;
						end
					end
			5'd1:	begin
						buffer <= d;
						rd <= 1;
						state <= 2;
					end
			5'd2:	begin
						if(txe == 0)begin
							wr <= 1;
							dout <= buffer;
							state <= 5'd3;
						end
					end
			5'd3:	begin
						wr <= 0;
						state <= 5'd4;
					end
			5'd4:	begin
						SI <= 0;
						state <= 5'd5;
					end	
			5'd5:	begin
						SI <= 1;
						state <= 5'd0;
					end						
			default:state <= 0;
		endcase
		//led[2:0]<=dout[2:0];
	end
		assign d = (state==5'd3)?dout:8'bzzzz_zzzz;

	clk2	clk2_inst (
	.inclk0 ( clk ),
	.c0 ( clk_40M ),
	.c1 ( clk_125M )
	);
	///////////////////////////////////////////////AD///////////////////////////////////////
	reg [9:0]AD_A_buf/*synthesis noprune*/ ;
	reg [9:0]AD_B_buf/*synthesis noprune*/ ;
	/*
	always @(posedge clk_40M)
	begin
		AD_A_buf <= AD_A;
		AD_B_buf <= AD_B;
	end
	
	assign AD_ECODE_A = ~clk_40M;
	assign AD_ECODE_B = ~clk_40M;
	
	assign AD_S1 = 1;
	assign AD_S2 = 0;
	assign AD_DFS_GAIN = 1;
*/
	////////////////////////////////////////////////DA/////////////////////////////////////
	initial led<=1;
	reg p5;
	reg clear_key;
	reg [32:0] cnt;
	reg q,buff0,buff1;
	reg e;
	initial cnt<=0;
	initial p5<=0;
	always @ (posedge clk)
	begin 
		if(cnt==119999) begin
			p5<=1;
			cnt<=0;
		end
		else begin
		  p5<=0;
		  cnt<=cnt+1;
		end
	end
	always @ (posedge clk) begin
		if(p5==1) begin 
			buff0<=key;
			buff1<=buff0;
		end
		if(buff0==buff1)
			clear_key<=buff0;
	end
	always @(posedge clk) begin 
		q<=clear_key;
		if({q,clear_key}==1)
			e<=1;
		else 
			e<=0;
	end

	reg [15:0]address;
	wire [13:0]sin_w;
	wire [13:0]tri_w;
	wire [13:0]squ_w;
	reg[2:0] stat;
	initial stat = 1;
	reg pre;
	always @(posedge clk) begin
		if (e == 1) begin
			led <= {led[1:0], led[2]};
			stat <= {stat[1:0], stat[2]};
		end
	end
	always @(posedge clk_125M)
	begin
		address <= address + 16'd2621;
		case(stat)
			1: begin
				DA_A <= sin_w;
				DA_B <= sin_w;
			end
			2: begin
				DA_A <= tri_w;
				DA_B <= tri_w;
			end
			4: begin
				DA_A <= squ_w;
				DA_B <= squ_w;
			end
		endcase
	end
	assign DA_CLK_A = clk_125M;
	assign DA_CLK_B = clk_125M;
	assign DA_WR_A = ~clk_125M;
	assign DA_WR_B = ~clk_125M;
	
	sin_table INS_SIN(
	.address(address[15:7]),
	.data(sin_w)
   );
	tri_table INS_TRI(
	.address(address[15:7]),
	.data(tri_w)
   );
	squ_table INS_SQU(
	.address(address[15:7]),
	.data(squ_w)
   );
endmodule 
