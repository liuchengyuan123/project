using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

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
    }
}
