from discord.ext import menus, commands


class EmbedPaginator(menus.MenuPages):
    def __init__(self, ctx : commands.Context, menu : menus.MenuPages):
        self.ctx = ctx
        self.started = False
        self.menu = menu

    async def run(self, **kwargs):
        await self.menu.start(self.ctx, **kwargs)
        self.started = True


class PaginatorPageSource(menus.ListPageSource):
    async def format_page(self, _, page):
        return page