# Script principal para o proxy
import asyncio
import aiohttp
import json
from aiohttp import web

class ProxyServer:
  def __init__(self, config_file):
    with open(config_file) as f:
      self.config = json.load(f)
    self.routes = self.config['routes']

  async def handle(self, request):
    target_url = self._get_target_url(request)
    if not target_url:
      return web.Response(text="No route found", status=404)

    async with aiohttp.ClientSession() as session:
      async with session.request(
        request.method,
        target_url,
        headers=request.headers,
        data=await request.read()
    
      ) as response:
        body = await response.read()
        return web.Response(
          body=body,
          status=response.status,
          headers=dict(response.headres)

        )

def _get_target_url(self, request):
  for route in self.routes:
    if request.host == route['host']:
      return f"{route['scheme']}://{route['target_host']}:{route['target_port']}{request.path_qs}"
  return None

async def start(self):
  app = web.Application()
  app.router.add_route('*', '/{tail:.*}', self.handle)
  runner = web.AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, self.config['listen_address'], self.config['listen_port'])
  await site.start()

if __name__ == '__main__':
  server = ProxyServer('config.json')
  loop = asyncio.get_event_loop()
  loop.run_until_complete(server.start())
  loopr.run_forever()
  

        
