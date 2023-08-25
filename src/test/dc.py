import asyncio
from typing import Optional

from nonebot.adapters.discord.api import User
from nonebot.adapters.discord.commands import CommandOption
from arclet.alconna import Args, Option, Alconna, CommandMeta

from nonebot_plugin_alconna.adapters.discord import MentionUser, translate

matcher = translate(
    Alconna(
        "permission",
        Option("add", Args["plugin#插件名", str]["priority#优先级;?", int]),
        Option("remove", Args["plugin#插件名", str]["time#时长;?", float]),
        Option("ban", Args["user#用户;?", MentionUser]),
        meta=CommandMeta("权限管理"),
    )
)


@matcher.handle_sub_command("add")
async def handle_user_add(
    plugin: CommandOption[str], priority: CommandOption[Optional[int]]
):
    await matcher.send_deferred_response()
    await asyncio.sleep(2)
    await matcher.edit_response(f"你添加了插件 {plugin}，优先级 {priority}")
    await asyncio.sleep(2)
    fm = await matcher.send_followup_msg(
        f"你添加了插件 {plugin}，优先级 {priority} (新消息)",
    )
    await asyncio.sleep(2)
    await matcher.edit_followup_msg(
        fm.id,
        f"你添加了插件 {plugin}，优先级 {priority} (新消息修改后)",
    )


@matcher.handle_sub_command("remove")
async def handle_user_remove(
    plugin: CommandOption[str], time: CommandOption[Optional[float]]
):
    await matcher.send(f"你移除了插件 {plugin}，时长 {time}")


@matcher.handle_sub_command("ban")
async def handle_admin_ban(user: CommandOption[User]):
    await matcher.finish(f"你禁用了用户 {user.username}")