from fastapi import FastAPI
from sales.sales_functions import *
from sales.sales_schema import Sale

app = FastAPI()


# ------------------------------------- SALE -------------------------------------

@app.get("/sales", tags=["Sale Methods"], description="Get all sales")
async def get_sales():
    return get_all_sales()


@app.get("/sales/{sale_id}", tags=["Sale Methods"], description="Get sale by id")
def get_sale(sale_id: str):
    return get_sale_by_id(sale_id)


@app.post("/sales/{sale_id}", tags=["Sale Methods"], description="Create new sale")
def post_sale(sale: Sale):
    return new_sale(sale)


@app.put("/sales/{sale_id}", tags=["Sale Methods"], description="Update sale")
def put_sale(sale: Sale):
    return update_sale(sale)


@app.delete("/sales/{sale_id}", tags=["Sale Methods"],
            description="Delete sale by sale, if sale is not in order_status")
def delete_sale_by_id(sale_id: str):
    return delete_sale(sale_id)

# ------------------------------------- SALE -------------------------------------