from covid import set_i18n

set_i18n("pt_BR.UTF-8")
from covid.ui import calc

ui = calc.CalcUI()
ui.run()