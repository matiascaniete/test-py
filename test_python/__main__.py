import pendulum
from icecream import ic
from loguru import logger
from rich.console import Console
from rich.markdown import Markdown
import argparse
import tqdm
import time
from pydantic import BaseModel
import httpx

parser = argparse.ArgumentParser(prog="hello", description="Hello world")
parser.add_argument("-p", "--progress", action="store_true", help="Show progress")

args = parser.parse_args()

if args.progress:
    for _ in tqdm.tqdm(range(20)):
        # wait 0.1 seconds
        time.sleep(0.1)
    exit()

data = {"claca": 1, "test": "test text"}


class MyModel(BaseModel):
    claca: int
    test: int


try:
    MyModel(**data)
except Exception as e:
    ic(e.errors())

markdown = """
# this is header

Rich is great

1. item
2. item 2

```bash
echo "Hello, World"
```
"""

ic("Printing with icecream")
now = pendulum.now("UTC")
ic(now)
ic(data)

logger.info("Logging with loguru")

console = Console()
console.print("Printing with rich")
console.print(Markdown(markdown))

response = httpx.get(
    "https://erp.ndorma.com", headers={"User-Agent": "Mozilla/5.0"}, follow_redirects=True
)

print(response.text)
