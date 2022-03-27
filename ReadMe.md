# Install Requirements
```
$ pip install -r requirements.txt
```
# Run

```
$ python server.py
```

# API
```
port = 4800
```
## POST Request
Request Path
```
/course/search 
```
Request Body(JSON)
```
{
  "type": <can be 'a' or 'o'>,
  "result": {
    <can be "A","B",... or "S">: <count of result>
  }
}
```

## Example

URL
```
http://localhost:4800/course/search
```

Request Body(JSON)
```
{
    "type": "o",
    "result": {
        "A": 3,
        "B" : 6
    }
}
```
