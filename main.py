from covid.models import RSEICHA

def simulation_data_http(request):
  region = request.args.get('region', 'Brazil')
  m = RSEICHA(region=region)
  run = m.run()
  
  return run.data.to_json()
