from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from functions import bsm,rh,bthe,error_branching,itera,mixing,error_mixing,itera_mix,decay_ratios,decay_bsm,error_kpi,itera_kpi

g_gev = (1.1663787e-5)**2
hbar_gev = 6.582119514e-25
g_mev = (1.1663787e-11)**2
hbar_mev = 6.582119514e-22

################ LEPTONIC DECAY

m_bplus, m_bplus_err = [5.27933,[0.00013,-0.00013]]
m_dplus, m_dplus_err = [1.86965,[0.00005,-0.00005]]
m_dsplus, m_dsplus_err = [1.96834,[0.00007,-0.00007]]
m_K, m_K_err = [0.493677,[0.000016,-0.000016]]
m_pi, m_pi_err = [0.13957061,[0.00000024,-0.00000024]]
m_tau, m_tau_err = [1.77686,[0.00012,-0.00012]]
m_mu, m_mu_err = [0.1056583745,[0.0000000024,-0.0000000024]]
m_u, m_u_err = [0.00216,[0.00049,-0.00026]]
m_d, m_d_err = [0.00467,[0.00048,-0.00017]]
m_s, m_s_err = [0.093,[0.011,-0.005]]
m_c, m_c_err = [1.27,[0.02,-0.02]]
m_b, m_b_err = [4.18,[0.03,-0.02]]

Vub, Vub_err = [0.003746,[0.00009,-0.000062]]
Vcd, Vcd_err = [0.224608,[0.000254,-0.00006]]
Vcs, Vcs_err = [0.973526,[0.00005,-0.000061]]
Vus, Vus_err = [0.224745,[0.000254,-0.000059]]
Vud, Vud_err = [0.974410,[0.000014,-0.000058]]

f_bplus, f_bplus_err = [0.190,[0.0013,-0.0013]]
f_dplus, f_dplus_err = [0.212,[0.0007,-0.0007]]
f_dsplus, f_dsplus_err = [0.2499,[0.0005,-0.0005]]
f_Kpi, f_Kpi_err = [1.1928,[0.0026,-0.0026]]

delt_kpi, delt_kpi_err = [-0.0069,[0.0017,-0.0017]]
delt_kpitau, delt_kpitau_err = [0.0003,[0,0]]

tau_bplus, tau_bplus_err = [(1.638e-12)/hbar_gev,[(0.004e-12)/hbar_gev,-(0.004e-12)/hbar_gev]]
tau_dplus, tau_dplus_err = [(1040e-15)/hbar_gev,[(7e-15)/hbar_gev,-(7e-15)/hbar_gev]]
tau_dsplus, tau_dsplus_err = [(504e-15)/hbar_gev,[(4e-15)/hbar_gev,-(4e-15)/hbar_gev]]

bplus_exp, bplus_err_exp = [1.09e-4,[0.24e-4,-0.24e-4]]
dplus_exp, dplus_err_exp = [3.82e-4,[0.33e-4,-0.33e-4]]
dsplus_exp, dsplus_err_exp = [0.0548,[0.0023,-0.0023]]
kpi_exp, kpi_exp_err = [1.337,[0.0032,-0.0032]]
kpitau_exp, kpitau_exp_err = [6.438e-2,[9.384e-4,-9.384e-4]]

# B+ -> tau+ nu
mH_bplus, tanb_bplus = itera(m_bplus,m_bplus_err,m_tau,m_tau_err,Vub,Vub_err,f_bplus,f_bplus_err,tau_bplus,tau_bplus_err,m_u,m_u_err,m_b,m_b_err,bplus_exp,bplus_err_exp)

#plt.figure()
plt.scatter(tanb_bplus,mH_bplus,c='green',marker=',')
plt.ylabel('$\\log[m_{H+}$, GeV]')
plt.xlabel('$\\log[\\tan(\\beta)]$')
plt.title('$B^+\\to\\tau^+\\nu$')
#plt.show()

# D+ -> mu+ nu
mH_dplus, tanb_dplus = itera(m_dplus,m_dplus_err,m_mu,m_mu_err,Vcd,Vcd_err,f_dplus,f_dplus_err,tau_dplus,tau_dplus_err,m_c,m_c_err,m_d,m_d_err,dplus_exp,dplus_err_exp)

#plt.figure()
plt.scatter(tanb_dplus,mH_dplus,c='green',marker=',')
plt.ylabel('$\\log[m_{H+}$, GeV]')
plt.xlabel('$\\log[\\tan(\\beta)]$')
plt.title('$D^+\\to\\mu^+\\nu$')
plt.axis([-1,2,0,3])
#plt.show()

# Ds+ -> tau+ nu
mH_dsplus, tanb_dsplus = itera(m_dsplus,m_dsplus_err,m_tau,m_tau_err,Vcs,Vcs_err,f_dsplus,f_dsplus_err,tau_dsplus,tau_dsplus_err,m_c,m_c_err,m_s,m_s_err,dsplus_exp,dsplus_err_exp)

#plt.figure()
plt.scatter(tanb_dsplus,mH_dsplus,c='green',marker=',')
plt.ylabel('$\\log[m_{H+}$, GeV]')
plt.xlabel('$\\log[\\tan(\\beta)]$')
plt.title('$D_s^+\\to\\tau^+\\nu$')
#plt.show()

# (K -> mu)/(pi -> mu) + (tau -> K)/(tau -> pi)
#mH_kpi, tanb_kpi, 
mH2, tanb2 = itera_kpi(m_K,m_K_err,m_pi,m_pi_err,m_mu,m_mu_err,m_tau,m_tau_err,Vus,Vus_err,Vud,Vud_err,f_Kpi,f_Kpi_err,delt_kpi,delt_kpi_err,delt_kpitau,delt_kpitau_err,m_s,m_s_err,m_d,m_d_err,m_u,m_u_err,kpi_exp,kpi_exp_err,kpitau_exp,kpi_exp_err)

#plt.figure()
#plt.scatter(tanb_kpi,mH_kpi,c='green',marker=',')
#plt.ylabel('$\\log[m_{H+}$, GeV]')
#plt.xlabel('$\\log[\\tan(\\beta)]$')
#plt.title('$K\\to\\mu\\nu/\\pi\\to\\mu\\nu$ & $\\tau\\to K\\nu/\\tau\\to\\pi\\nu$')
#plt.show()

#plt.figure()
plt.scatter(tanb2,mH2,c='green',marker=',')
plt.ylabel('$\\log[m_{H+}$, GeV]')
plt.xlabel('$\\log[\\tan(\\beta)]$')
plt.title('$K\\to\\mu\\nu/\\pi\\to\\mu\\nu$ & $\\tau\\to K\\nu/\\tau\\to\\pi\\nu$')
#plt.show()

###############   MIXING

mt, mt_err = [172.9e3,[0.4e3,-0.4e3]]
mW, mW_err = [80.379e3,[0.012e3,-0.012e3]]
mBd, mBd_err = [5279.64,[0.13,-0.13]]
mBs, mBs_err = [5366.88,[0.17,-0.17]]

Vts, Vts_err = [0.04169,[0.00028,-0.00108]]
Vtd, Vtd_err = [0.00871,[0.000086,-0.000246]]
Vtb, Vtb_err = [0.999093,[0.000049,-0.000013]]

etaB, etaB_err = [0.551,[0.0022,-0.0022]]

fBs, fBs_err = [230.3,[1.3,-1.3]]
fBd, fBd_err = [190,[1.3,-1.3]]

BBs, BBs_err = [1.327,[0.046,-0.046]]
BBd, BBd_err = [1.318,[0.35,-0.35]]

delt_md, delt_md_err = [0.5064e12,[0.0019e12,-0.0019e12]]
delt_ms, delt_ms_err = [17.757e12,[0.021e12,-0.021e12]]
delt_md_expect, delt_md_err_exp = [0.533e12,[0.022e12,-0.036e12]]
delt_ms_expect, delt_ms_err_exp = [18.4e12,[0.7e12,-1.2e12]]

# B0d mixing
mH_md, tanb_md = itera_mix(mt,mt_err,mW,mW_err,Vtd,Vtd_err,Vtb,Vtb_err,etaB,etaB_err,mBd,mBd_err,fBd,fBd_err,BBd,BBd_err,delt_md,delt_md_err,delt_md_expect,delt_md_err_exp)

#plt.figure()
plt.scatter(tanb_md,mH_md,marker=',',c='green')
plt.axis([-1,2,0,3])
plt.ylabel('$\\log[m_{H+}$, GeV]')
plt.xlabel('$\\log[\\tan(\\beta)]$')
plt.title('$B^0_d-\\bar{B}^0_d$')
#plt.show()

# B0s mixing
mH_ms, tanb_ms = itera_mix(mt,mt_err,mW,mW_err,Vts,Vts_err,Vtb,Vtb_err,etaB,etaB_err,mBs,mBs_err,fBs,fBs_err,BBs,BBs_err,delt_ms,delt_ms_err,delt_ms_expect,delt_ms_err_exp)

#plt.figure()
plt.scatter(tanb_ms,mH_ms,marker=',',c='green')
plt.axis([-1,2,0,3])
plt.ylabel('$\\log[m_{H+}$, GeV]')
plt.xlabel('$\\log[\\tan(\\beta)]$')
plt.title('$B^0_s-\\bar{B}^0_s$')
#plt.show()



###################### b to s gamma


###################### GLOBAL CONSTRAINT

h = np.linspace(0,3,300)
t = np.linspace(-1,2,300)
hl = []
tl = []

for i in range(len(h)):
    for j in range(len(t)):
        hb = np.where(mH_bplus==h[i])[0]# and tanb_bplus==t[j]))[0]
        hd = np.where(mH_dplus==h[i])[0]# and tanb_dplus==t[j]))[0]
        hds = np.where(mH_dsplus==h[i])[0]# and tanb_dsplus==t[j]))[0]
        hkpi = np.where(mH2==h[i])[0]# and tanb2==t[j]))[0]
        hmd = np.where(mH_md==h[i])[0]# and tanb_md==t[j]))[0]
        hms = np.where(mH_ms==h[i])[0]# and tanb_ms==t[j]))[0]
        
        lb,ld,lds,lkpi,lmd,lms = [],[],[],[],[],[]
        for k in range(len(hb)):
            if tanb_bplus[hb[k]] == t[j]:
                lb = np.append(lb,hb[k])
        for l in range(len(hd)):
            if tanb_dplus[hd[l]] == t[j]:
                ld = np.append(ld,hd[l])
        for m in range(len(hds)):
            if tanb_dsplus[hds[m]] == t[j]:
                lds = np.append(lds,hds[m])
        for n in range(len(hkpi)):
            if tanb2[hkpi[n]] == t[j]:
                lkpi = np.append(lkpi,hkpi[n])
        for o in range(len(hmd)):
            if tanb_md[hmd[o]] == t[j]:
                lmd = np.append(lb,hmd[o])
        for p in range(len(hms)):
            if tanb_ms[hms[p]] == t[j]:
                lms = np.append(lms,hms[p])

        if len(lb) > 0 and len(ld) > 0 and len(lds) > 0 and len(lkpi) > 0 and len(lmd) > 0 and len(lms) > 0:
            hl = np.append(hl,h[i])
            tl = np.append(tl,t[j])

plt.figure()
plt.scatter(tl,hl,c='orange')
plt.axis([-1,2,0,3])
plt.ylabel('$\\log[m_{H+}$, GeV]')
plt.xlabel('$\\log[\\tan(\\beta)]$')
plt.title('Global Fit')
plt.show()



#plt.show()










