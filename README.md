# Website Server Status
![image](https://user-images.githubusercontent.com/78034307/111272989-9f314000-8676-11eb-9a0a-6da001996d9d.png)


## About
The front-end is developed using Bootstrap, and the back-end is developed using Python3 with Flask and jinja2.

##Sstructure

main_example.py
```python
  import requests
  
  resp = "https://example.com/"
  try:
    requests.get(resp, timeout=1) 
  except requests.exceptions.ConnectionError: 
    result = "error"
    print("error")
  else:
    result = "success"
    print("success")
    
```

index.html
```html
~~~
<body>
  {% if result == "error" %}
  <p>Connection Error</p>
  {% elif result == "success" %}
  <p>Connection success</p>
</body>
~~~
```

Use the `requests` library to get the http response. if `requests.get` returns a number 20X, it will output success; if not, it will output error.
Place a `result` variable in each process and change it according to the response.
Although it is omitted here, jinja2 will pass `result` to the html file.

It shows the uptime status by changing what is displayed depending on the contents of `result`.
This server status lists it, and you can easily add more servers to be monitored later. 


## Libraries
- Flask
- jinja2
- requests
Other dependent libraries are required.

# License
The source code is licensed MIT. The website content is licensed CC BY 4.0,see LICENSE.
