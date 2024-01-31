# API Documentation

## Fihirana API

This API provides endpoints to access and search through a collection of hira (`fihirana` in Malagasy) organized by their categories (`fihirana_name`).

### Endpoints

#### 1. Get All Fihirana

**Endpoint:** `/api/fihirana/all`  
**Method:** `GET`

**Description:** Returns a JSON object containing all the hira categorized by their respective names.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/fihirana/all
```

**Example Response:**

```json

```

#### 2. Get Hira by Fihirana

**Endpoint:** `/api/fihirana/<fihirana_name>`  
**Method:** `GET`

**Description:** Returns a JSON object containing all hira for a specific `fihirana_name`.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/fihirana/fihirana_dera
```

**Example Response:**

```json

```

#### 3. Search All Hira

**Endpoint:** `/api/fihirana/search`  
**Method:** `GET`

**Query Parameters:**

- `q`: Search term

**Description:** Searches all hira across different categories and returns matching results.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/fihirana/search?q=example
```

**Example Response:**

```json

```

#### 4. Search Hira in Fihirana

**Endpoint:** `/api/fihirana/<fihirana_name>/search`  
**Method:** `GET`

**Query Parameters:**

- `q`: Search term

**Description:** Searches hira within a specific `fihirana_name` category and returns matching results.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/fihirana/fihirana_dera/search?q=example
```

**Example Response:**

```json
[{ "title": "Example Hira 1" }, { "title": "Example Hira 2" }]
```

#### 5. Get Hira

**Endpoint:** `/api/fihirana/<fihirana_name>/get`  
**Method:** `GET`

**Query Parameters:**

- `title`: Title of the hira to retrieve

**Description:** Retrieves a specific hira within a given `fihirana_name` category.

**Example Request:**

```bash
curl -X GET http://your-api-url/api/fihirana/fihirana_dera/get?title=Example%20Hira%201
```

**Example Response:**

```json
{ "title": "Example Hira 1" }
```

### Running the API

To run the API, execute the following command in your terminal:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/` by default. Make sure to update the base URL in the examples accordingly.
