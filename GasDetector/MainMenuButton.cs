using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;

public class MainMenuButton : MonoBehaviour {

    public void PlayButton()
    {
        Debug.Log("Play Button hitted!");
    }

    public void SettingButton()
    {
        Debug.Log("Setting Button hitted!");
        SceneManager.LoadScene("SettingMenu");
    }

    public void PracticeButton()
    {
        Debug.Log("Practice Button hitted!");
        FileInfo t = new FileInfo("Assets/PracticeProcess.txt");
        StreamWriter sw = t.CreateText();
        sw.WriteLine("False");
        sw.WriteLine("1");
        sw.WriteLine("0");
        sw.WriteLine("False");
        sw.WriteLine("1");
        sw.Close();
        sw.Dispose();
        SceneManager.LoadScene("PracticeMenu");
    }
}
