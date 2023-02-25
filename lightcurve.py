from astropy.io import fits, ascii
from astropy.time import Time
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd
import mpl_style


plt.style.use(mpl_style.greyfox)
fname = 'kplr012644769-20160128150956_dvt.fits'
hdu = fits.open(f'data/{fname}')
data = hdu[1].data
df = pd.DataFrame({'time': data['TIME'], 'flux': data['LC_INIT']})
df['time'] = Time(df['time'] + 2454833, format='jd').datetime64
plt.plot(df['time'], df['flux'], '.', ms=3, label=fname)

fname = 'kplr012644769_q1_q16_tce_01_dvt_lc.tbl'
data = ascii.read(f'data/{fname}')
df = pd.DataFrame({'time': data['TIME'], 'flux': data['INIT_FLUX_PL']})
df['time'] = Time(df['time'] + 2454833, format='jd').datetime64
plt.plot(df['time'], df['flux'], '.', ms=3, c='C0', label=fname)

plt.title('Kepler-16 System', size=16)
plt.xlabel(r'Date ($P_{orb}=41.0778$ days)', size=16)
plt.ylabel(r'Flux ($F_e/F_o - 1$)', size=16)

date_form = DateFormatter("%b %Y")
plt.gca().xaxis.set_major_formatter(date_form)

plt.xticks(rotation=45)
plt.grid(ls=':')
plt.legend(markerscale=4)
plt.tight_layout()
plt.savefig('kepler-16.png', dpi=300)