using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class ExtraController : MonoBehaviour {
    public Text q1, q2, q3;
    float Mesh, CO2, MeshAndCo2;
	// Use this for initialization
	void Start () {
        read_from_file();
        q1 = GameObject.Find("Question1").GetComponent<Text>();
        q2 = GameObject.Find("Question2").GetComponent<Text>();
        q3 = GameObject.Find("Question3").GetComponent<Text>();
        string x = string.Format("{0}{1}{2}{3}{4}", "已知甲烷气体浓度", Mesh.ToString(), "，二氧化碳和甲烷 ", MeshAndCo2.ToString(), "，则二氧化碳浓度为？");
        Debug.Log(x);
        q1.text = x;
	}
	
	// Update is called once per frame
	void Update () {
		
	}

    void read_from_file()
    {
        FileInfo t = new FileInfo("Assets/Dense.in");
        StreamReader sr = File.OpenText("Assets/Dense.in");
        string line;
        line = sr.ReadLine();
        CO2 = float.Parse(line);
        line = sr.ReadLine();
        Mesh = float.Parse(line);
        MeshAndCo2 = Mesh + CO2 / (float)0.955;
        Debug.Log(CO2);
        Debug.Log(Mesh);
        Debug.Log(MeshAndCo2);
        sr.Close();
        sr.Dispose();
    }
}
