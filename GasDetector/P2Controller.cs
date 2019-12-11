using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using TMPro;
using UnityEngine.UI;


public class P2Controller : MonoBehaviour {

    bool RezeroDone, ReadDone;
    float RezeroError, ReadError, stdv;
    int pushcnt;
    Slider RezeroBar, stdBar, ReadBar;

    // Use this for initialization
    void Start () {
        read_from_file();
        RezeroBar = GameObject.Find("Slider1").GetComponent<Slider>();
        stdBar = GameObject.Find("Slider2").GetComponent<Slider>();
        ReadBar = GameObject.Find("Slider3").GetComponent<Slider>();
        if (RezeroDone)
        {
            RezeroBar.value = (float)0.5;
            GameObject.Find("RezeroNum").GetComponent<TMP_Text>().text = "0";
        }
        else
        {
            GameObject.Find("RezeroNum").GetComponent<TMP_Text>().text = (RezeroBar.value - (float)0.5).ToString();
        }
        stdBar.value = stdv;
	}
	
	// Update is called once per frame
	void Update () {
		
	}

    public void Slider1Changed()
    {
        GameObject.Find("RezeroNum").GetComponent<TMP_Text>().text = (RezeroBar.value - 0.5).ToString();
    }

    public void Slider3Changed()
    {
        GameObject.Find("ReadNum").GetComponent<TMP_Text>().text = ReadBar.value.ToString();
    }

    public void DisableRezero()
    {
        if (RezeroDone)
        {
            Debug.Log("You have done rezero!");
            return;
        }
    }

    public void DisableRead()
    {
        if (!RezeroDone)
        {
            Debug.Log("You haven't rezero!");
            return;
        }
    }

    public void SubmitCalled()
    {
        float val = System.Math.Abs(RezeroBar.value - 0.5f) / 0.5f;
        if (!RezeroDone)
            RezeroDone = true;
        else
        {
            ReadDone = true;
            val = RezeroError;
        }
        WriteIntoFile(val);

        Debug.Log("Back to PracticeMenu!");
        SceneManager.LoadScene("PracticeMenu");
    }

    void WriteIntoFile(float val)
    {
        FileInfo t = new FileInfo("Assets/PracticeProcess.txt");
        StreamWriter sw = t.CreateText();
        sw.WriteLine(RezeroDone.ToString());
        sw.WriteLine(val);
        sw.WriteLine(pushcnt.ToString());
        sw.WriteLine(ReadDone.ToString());
        sw.WriteLine(System.Math.Min(System.Math.Abs(ReadBar.value - stdv) / stdv, 1f));
        sw.Close();
        sw.Dispose();
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

        t = new FileInfo("Assets/Dense.in");
        sr = File.OpenText("Assets/Dense.in");
        line = sr.ReadLine();
        stdv = float.Parse(line);
        sr.Close();
        sr.Dispose();
    }
}
