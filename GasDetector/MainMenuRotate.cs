using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainMenuRotate : MonoBehaviour {

    public GameObject main;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        main.transform.Rotate(new Vector3(0, 1, 0));
	}
}
