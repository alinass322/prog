import typer

from moduls import dec_zam, gen, rec

app = typer.Typer()


@app.comand()
def gen(name: gen, seq: str = typer.Option()):
    print(def)