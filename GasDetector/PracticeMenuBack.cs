using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class PracticeMenuBack : MonoBehaviour {

	public void BackToMainMenu()
    {
        SceneManager.LoadScene("MainMenu");
    }

    public void Forward ()
    {
        Vector3 v = GameObject.Find("Main Camera").transform.position;
        GameObject.Find("Main Camera").transform.position = new Vector3(v.x, v.y, v.z + 796f);
    }

    public void Backward ()
    {
        Vector3 v = GameObject.Find("Main Camera").transform.position;
        GameObject.Find("Main Camera").transform.position = new Vector3(v.x, v.y, v.z - 796f);
    }
}
