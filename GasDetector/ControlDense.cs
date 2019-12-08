using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.IO;

public class ControlDense : MonoBehaviour {

    // Use this for initialization
    Slider CO2Bar, MeshGasBar, CO2aGasBar;
	void Start () {
        CO2Bar = GameObject.Find("CO2Bar").GetComponent<Slider>();
        MeshGasBar = GameObject.Find("MeshGasBar").GetComponent<Slider>();
        CO2aGasBar = GameObject.Find("CO2&GasBar").GetComponent<Slider>();
        Debug.Log(CO2Bar.value);
        Debug.Log(MeshGasBar.value);
        Debug.Log(CO2aGasBar.value);
        read_from_file();
    }
    
    public void CO2Changed()
    {
        GameObject.Find("CO2Value").GetComponent<TMP_Text>().text = CO2Bar.value.ToString();
        CO2aGasChanged();
    }
    public void MeshGasChanged()
    {
        GameObject.Find("MeshGasValue").GetComponent<TMP_Text>().text = MeshGasBar.value.ToString();
        CO2aGasChanged();
    }
    public void CO2aGasChanged()
    {
        float val = MeshGasBar.value + CO2Bar.value / (float)0.955;
        CO2aGasBar.value = val;
        GameObject.Find("CO2&MeshGasValue").GetComponent<TMP_Text>().text = CO2aGasBar.value.ToString();
    }
    void read_from_file()
    {
        FileInfo t = new FileInfo("Assets/Dense.in");
        StreamReader sr = File.OpenText("Assets/Dense.in");
        string line;
        line = sr.ReadLine();
        CO2Bar.value = float.Parse(line);
        line = sr.ReadLine();
        MeshGasBar.value = float.Parse(line);
        CO2Changed();
        MeshGasChanged();
        /*
        string line;
        while ((line = sr.ReadLine()) != null)
        {
            string[] msg = line.Split(',');
            Vector3 p;
            p.x = float.Parse(msg[0]);
            p.y = float.Parse(msg[1]);
            p.z = float.Parse(msg[2]);
            Debug.Log(p);

            fjw[++p_tot] = Instantiate(obj, p, Quaternion.identity);
            Debug.Log(p_tot);
        }
        */
        sr.Close();
        sr.Dispose();
    }
}
