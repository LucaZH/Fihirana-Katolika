# API Documentation

## Fihirana API

This API provides endpoints to access and search through a collection of hira (`fihirana` in Malagasy) organized by their categories (`fihirana_name`).

### Endpoints

#### 1. Get All Fihirana

**Endpoint:** `/api/fihirana/`  
**Method:** `GET`

**Description:** Returns a JSON object containing all the hira categorized by their respective names.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/fihirana/
```

**Example Response:**

```json
{
  "status": "success",
  "data": {
    "ankalazao_ny_tompo": [...],
    "antsao_ny_tompo": [...],
    ...
  }
}
```

#### 2. Get or Search Hira by Fihirana

**Endpoint:** `/api/<fihirana_name>/`  
**Method:** `GET`

**Description:** Returns a JSON object containing all hira for a specific `fihirana_name`. Optionally, you can provide a `search` parameter to search for specific hira within the category.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/fihirana_dera
```

**Example Response:**

```json
{
  "status": "success",
  "data": [
    {
      "page": "7",
      "title": "Ianao ilay nirahina hanasitrana ny fo mivalo"
    },
    {
      "page": "40",
      "title": "Miankohofa mba hitsaoka"
    },
    ...
  ]
}
```

#### 3. Search All Hira

**Endpoint:** `/api/hira/`  
**Method:** `GET`

**Query Parameters:**

- `search`: Search term

**Description:** Searches all hira across different categories and returns matching data.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/hira/?search=Ianao ilay nirahina hanasitrana ny fo mivalo
```

**Example Response:**

```json
{
  "status": "success",
  "data": {
    "fihirana_dera": [
      {
        "title": "Ianao ilay nirahina hanasitrana ny fo mivalo"
      },
      {
        "title": "Jesoa mpamindra fo"
      },
      {
        "title": "Ahiratray ny masonay"
      },
      {
        "title": "Jerosalema, ianao Si\u00f4na"
      },
      {
        "title": "Tsarovy, ry Iaveh, ilay fanekena nataonao fahiny tamin'ny vahoakanao"
      }
    ],
    ...
  }
}
```

#### 4. Get Hira

**Endpoint:** `/api/<fihirana_name>/hira`  
**Method:** `GET`

**Query Parameters:**

- `title`: Title of the hira to retrieve

**Description:** Retrieves a specific hira within a given `fihirana_name` category.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/ankalazao_ny_tompo/?search=Tsy ny (ahiahy) ahiahin'izao tontolo izao
```

**Example Response:**

```json
{
  "status": "success",
  "data": [
    {
      "page": "534",
      "title": "Tsy ny (ahiahy) ahiahin'izao tontolo izao"
    },
    ...
  ]
}
```
