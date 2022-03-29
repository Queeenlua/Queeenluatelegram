import asyncio
from collections import deque

from . import ALIVE_NAME, catub, edit_or_reply


from uuid import uuid4

plugin_category = "Queen main"

@catub.cat_cmd(
    pattern="XX$",
    command=("XX", plugin_category),
    info={
        "header": "XX animation",
        "usage": "{tr}XX",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "XX")
    deq = deque(list("🌑🌒🌓🌔🌕🌖🌗🌘"))
    for _ in range(999):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)