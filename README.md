# ECOMMERCE DJANGO REST API'S

## Requirements
1. Django==4.2
2. django-filter==23.1
3. djangorestframework==3.14.0
4. drf-nested-routers==0.93.4

### Installation
    ``` python3 -m venv venv```
    ```pip3 install -r requirements.txt```

### API's 

1. Category API's

```
1. Create Category
------------------
API : localhost:8080/api/categories/
Method : POST
Sample Body
    {
        "name":"Dress Wear2",
        "description":"Dress for mens, womens and childrens"
    }

2. List categories with pagination
----------------------------------
API : localhost:8080/api/categories?limit=10&offset=0
Method : GET

3. List categories with search params (search with both name, description etc..)
--------------------------------------------------------------------------------
API : localhost:8080/api/categories?limit=10&offset=0&search=Electronics
Method : GET
Response :
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Electronics",
            "description": "Long description"
        }
    ]
}

4. Update Category
------------------
API : localhost:8080/api/categories/{Category_id}/
Method : PUT
{
    "name":"updated_name",
    "description":"updated description"
}

5. Delete Category
------------------
API : localhost:8080/api/categories/{Category_id}/
Method : DELETE
```

2. Subcategory APIs

```
1. List all subcategories under category
API : localhost:8080/api/categories/{category_id}/subcategories/?limit=10&offset=0

2. List all subcategories under category with search params
API: localhost:8080/api/categories/2/subcategories/?search={search_params}&name={other_parms}
Method : GET

3. Create Subcategory under Category
API: localhost:8080/api/categories/{category_id}/subcategories/
Method : POST
body : 
{
    "name":"",
    "description": "",
    "category": category_id
}
4. Update Category Same API above and change method to PUT
5. Delete subcategory 
API : localhost:8080/api/categories/{category_id}/subcategories/{sub_category_id}
Method : DELETE
```


