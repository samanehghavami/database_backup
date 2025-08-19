import click,os,shutil
from datetime import datetime
@click.command()
@click.option("--type","-t",type=click.Choice(["mysql","postgresql"]),help="choose your database type")
@click.option("--host","-h",help="database hostname")
@click.option("--user","-u",help="database username")
@click.option("--password", "-P", prompt=True, hide_input=True, help="database password")
@click.option("--database","-d",help="databasenme fo backup")
@click.option("--path","-p",help="path of backup file")

def backup(type, host, user, password, database, path):
    """
    this is a simple tools for backup database
    """
    os.makedirs(path, exist_ok=True)
    date=datetime.now().strftime("%Y%m%d")
    filename=os.path.join(path,f"{database}_{date}.sql")
    if type == "mysql":
        cmd= f"mysqldump -h{host} -u{user} -p{password} {database} > {filename}"
    elif type == "postgresql":
        cmd = f"pg_dump -h {host} -U {user} -d {database} -f {filename}"
    
    else:
        click.secho("invalid database type",fg="red")
    
    if os.system(cmd) :
        click.secho("error in backup",fg="red")
    else:
        click.secho(f"database is successfully backedup in {filename}",fg="green")
    
if __name__ == "__main__":
    backup()
