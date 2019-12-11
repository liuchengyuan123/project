using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using TMPro;

public class ScoreDataController : MonoBehaviour
{

    bool RezeroDone, ReadDone;
    float RezeroError, ReadError;
    int pushcnt;

    // Use this for initialization
    void Start()
    {
        read_from_file();
        if (!RezeroDone)
            GameObject.Find("RezeroScore").GetComponent<TMP_Text>().text = "0/100";
        else
            GameObject.Find("RezeroScore").GetComponent<TMP_Text>().text = string.Format("{0:D}/100", 100 - (int)(RezeroError * 100));
        GameObject.Find("DetectScore").GetComponent<TMP_Text>().text = string.Format("{0:D}/100", pushcnt * 20);
        if (!ReadDone)
            GameObject.Find("ReadScore").GetComponent<TMP_Text>().text = "0/100";
        else
            GameObject.Find("ReadScore").GetComponent<TMP_Text>().text = string.Format("{0:D}/100", 100 - (int)(ReadError * 100));
    }

    // Update is called once per frame
    void Update()
    {

    }

    public void RezeroCalled()
    {
        if (RezeroDone)
        {
            Debug.Log("You have passed Rezero!");
            return;
        }
        Debug.Log("RezeroButton");
        SceneManager.LoadScene("P2Menu");
    }

    //DetectButton function should be fixed after importing module
    public void DetectCalled()
    {
        if (!RezeroDone)
        {
            Debug.Log("You haven't rezero!");
            return;
        }
        pushcnt = 5;
        Debug.Log("You have beat 5 times, detecting over!");
    }

    public void ReadCalled()
    {
        if (ReadDone)
        {
            Debug.Log("You have passed Read!");
            return;
        }
        if (pushcnt < 5)
        {
            Debug.Log("You haven't done Detect!");
            return;
        }
        Debug.Log("ReadButton");
        SceneManager.LoadScene("P2Menu");
    }

    void read_from_file()
    {
        FileInfo t = new FileInfo("Assets/PracticeProcess.txt");
        StreamReader sr = File.OpenText("Assets/PracticeProcess.txt");
        string line;
        line = sr.ReadLine();
        RezeroDone = bool.Parse(line);
        line = sr.ReadLine();
        RezeroError = float.Parse(line);
        line = sr.ReadLine();
        pushcnt = int.Parse(line);
        line = sr.ReadLine();
        ReadDone = bool.Parse(line);
        line = sr.ReadLine();
        ReadError = float.Parse(line);
        sr.Close();
        sr.Dispose();
    }
}
