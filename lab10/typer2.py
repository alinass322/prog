import typer
from moduls import dec_zam
from moduls import gen
from moduls import rec

app = typer.Typer()

@app.comand()
def gen(name: gen, seq: str = typer.Option()):
    print(def)


@app.command()
def dec_zam(*args: str):
    uv_func = unique_values_closure()
    result = uv_func(*args)
    print(dec_zam)


@app.command()
def rec(input_list: str):
    converted = rec.to_str(eval(input_list))
    print(rec)


def main():
    app()