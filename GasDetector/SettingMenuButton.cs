using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System;
using System.IO;
using UnityEngine.UI;

public class SettingMenuButton : MonoBehaviour {
    Slider CO2Bar, MeshGasBar;
    private void Start()
    {
        CO2Bar = GameObject.Find("CO2Bar").GetComponent<Slider>();
        MeshGasBar = GameObject.Find("MeshGasBar").GetComponent<Slider>();
    }

    public void BackButton()
    {
        write();
        Debug.Log("Back Button get hitted!");
        SceneManager.LoadScene("MainMenu");
    }

    void write()
    {
        FileInfo t = new FileInfo("Assets/Dense.in");
        StreamWriter sw = t.CreateText();
        string msg = CO2Bar.value.ToString();
        sw.WriteLine(msg);
        msg = MeshGasBar.value.ToString();
        sw.WriteLine(msg);
        sw.Close();
        sw.Dispose();
    }
}
