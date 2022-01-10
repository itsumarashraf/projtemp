from .models import *
from criminals.models import criminal



def seteducation(id,data):
    criminalid = criminal.getcriminal(id)
    education.objects.create(criminal =criminalid,school=data['school'],college=data['collage'],schoolFrom=data['schoolfrom'],
                             schoolTo=data['schoolto'], collegeFrom=data['collagefrom'],collegeTo=data['collageto']
                             )
    
def setcommunications(id,data):
    criminalid = criminal.getcriminal(id)
    communication.objects.create(criminal=criminalid,phone=data['phone'],landline=data['landline'],email=data['email'])

def setmarriagedetails(id,data):
    criminalid = criminal.getcriminal(id)
    if data['married']=='no':
        pass
    else:
        spouse.objects.create(criminal=criminalid,married=1,spouseName=data['spousename'],daughterof=data['spousefather'],occupation=data['spouseoccupaion'],
                              address=data['spouseaddress'],age=data['spouseage'],phone=data['spousephone'])
        
        kidnames = data.getlist('kidname')
        occ = data.getlist('kidoccupation')
        age = data.getlist('kidage')
        phone = data.getlist('kidphone')
        school = data.getlist('kidschool')
        collage = data.getlist('kidcollage')
        
        for n,o,a,p,s,c in zip(kidnames,occ,age,phone,school,collage):
            kids.objects.create(criminal=criminalid, kidName=n, occupation=o,age=a,phone=p,school=s,college=c)
            
def setfinancialdetails(id,data):
    criminalid = criminal.getcriminal(id)
    financialdetails.objects.create(criminal=criminalid,incomesource=data['incomesourse'],monthlyexpenses=data['monthlyincome'],propertyy=data['property'])

def setmobilitydetails(id,data):
    criminalid = criminal.getcriminal(id)
    vname = data.getlist('vehicalname')
    vregno = data.getlist('vehicalregno')
    vtype = data.getlist('vehicaltype')
    
    for vn,vr,vt in zip(vname,vregno,vtype):
        criminalid = criminal.getcriminal(id)
        mobility.objects.create(criminal=criminalid,vehicalName=vn,vehicalType=vt,registrationNo=vr)
        

def setparentdetails(id,data):
    criminalid = criminal.getcriminal(id)
    father.objects.create(criminal=criminalid,name=data['father'],occupation=data['fatheroccupation'],age=data['fatherage'],phone=data['fatherphone'])
   
    mother.objects.create(criminal=criminalid,name=data['mothername'],do=data['muncle'],age=data['motherage'],phone=data['munclephone'],occupation=data['muncleoccupationaladdress'],address=data['muncleaddress']) 

def setgrandparentdetails(id,data):
    criminalid = criminal.getcriminal(id)
    grandfather.objects.create(criminal=criminalid,name=data['pgfather'],address=data['pgfatheraddress'],phone=data['pgfatherphone'])
    grandmother.objects.create(criminal=criminalid,name=data['pgmothername'],do=data['pguncle'],address=data['pgmotheraddress'],phone=data['pgmotherphone'])
    
    maternalgrandfather.objects.create(criminal=criminalid,name=data['mgfather'],address=data['mgfatheraddress'],phone=data['mgfatherphone'])
    maternalgrandmother.objects.create(criminal=criminalid,name=data['maternalmothername'],do=data['mguncle'],address=data['mgmotheraddress'],phone=data['mgmotherphone'])
    
def setbrotherdetails(id,data):
    criminalid = criminal.getcriminal(id)
    bname=data.getlist('brother')
    bocc=data.getlist('brotheroccupation')
    bage=data.getlist('brotherage')
    bphone=data.getlist('brotherphone')
    
    for bn,bo,ba,bp in zip(bname,bocc,bage,bphone):
        binstance=brother.objects.create(criminal=criminalid,name=bn,occupation=bo,age=ba,phone=bp)
    
    wname=data.getlist('brotherswifename')
    wage=data.getlist('brotherswifeage')
    wphone=data.getlist('brotherswifephone')
    wfather=data.getlist('brotherswifefather')
    waddress=data.getlist('brotherswifeaddress')
    woccupation=data.getlist('brotherswifeoccupation')
    
    for wn,wa,wp,wf,wad,wo in zip(wname,wage,wphone,wfather,waddress,woccupation):
        brotherspouse.objects.create(brother=binstance,name=wn,phone=wp,age=wa,do=wf,address=wad,occupation=wo)
    
    kname=data.getlist('brotherskid')
    koccupation=data.getlist('brotherskidoccupation')
    kage=data.getlist('brotherskidage')
    kphone=data.getlist('brotherskidphone')
    kschool=data.getlist('brotherskidschool')
    kcollege=data.getlist('brotherskidcollege')
    
    for kn,ko,ka,kp,ks,kc in zip(kname,koccupation,kage,kphone,kschool,kcollege):
        brotherkids.objects.create(brother=binstance,name=kn,occupation=ko,age=ka,phone=kp,school=ks,college=kc)
        
    
def setsisterdetails(id,data):
    criminalid = criminal.getcriminal(id)
    sname=data.getlist('sister')
    socc=data.getlist('sisteroccupation')
    sage=data.getlist('sisterage')
    sphone=data.getlist('sisterphone')
    
    for sn,so,sa,sp in zip(sname,socc,sage,sphone):
        sinstance=sister.objects.create(criminal=criminalid,name=sn,occupation=so,age=sa,phone=sp)
    
    wname=data.getlist('sistersspousename')
    wage=data.getlist('sistersspouseage')
    wphone=data.getlist('sistersspousephone')
    wfather=data.getlist('sisterspousefather')
    waddress=data.getlist('sisterspouseaddress')
    woccupation=data.getlist('sistersspouseoccupation')
    
    for wn,wa,wp,wf,wad,wo in zip(wname,wage,wphone,wfather,waddress,woccupation):
        sisterspouse.objects.create(sister=sinstance,name=wn,phone=wp,age=wa,do=wf,address=wad,occupation=wo)
    
    kname=data.getlist('sisterkid')
    koccupation=data.getlist('sisterskidoccupation')
    kage=data.getlist('sistersskidage')
    kphone=data.getlist('sistersskidphone')
    kschool=data.getlist('sisterskidschool')
    kcollege=data.getlist('sisterskidcollege')
    
    for kn,ko,ka,kp,ks,kc in zip(kname,koccupation,kage,kphone,kschool,kcollege):
        sisterkids.objects.create(sister=sinstance,name=kn,occupation=ko,age=ka,phone=kp,school=ks,college=kc)
        

def setpaternaluncledetails(id,data):
    criminalid = criminal.getcriminal(id)
    pname=data.getlist('paternalunclename')
    pocc=data.getlist('paternaluncleoccupation')
    page=data.getlist('paternaluncleage')
    pphone=data.getlist('paternalunclephone')
    
    for pn,po,pa,pp in zip(pname,pocc,page,pphone):
        pinstance=uncle.objects.create(criminal=criminalid,name=pn,occupation=po,age=pa,phone=pp)
    
    wname=data.getlist('paternalunclespousename')
    wage=data.getlist('paternalunclespouseage')
    wphone=data.getlist('paternalunclespousephone')
    wfather=data.getlist('paternalunclespousefather')
    waddress=data.getlist('paternalunclespouseaddress')
    woccupation=data.getlist('paternalunclespousefatheroccupation')
    
    for wn,wa,wp,wf,wad,wo in zip(wname,wage,wphone,wfather,waddress,woccupation):
        unclespouse.objects.create(uncle=pinstance,name=wn,phone=wp,age=wa,do=wf,address=wad,occupation=wo)
    
    kname=data.getlist('paternalunclekid')
    koccupation=data.getlist('paternalunclekidoccupation')
    kage=data.getlist('paternalunclekidage')
    kphone=data.getlist('paternalunclekidphone')
    kschool=data.getlist('paternalunclekidschool')
    kcollege=data.getlist('paternalunclekidcollege')
    
    for kn,ko,ka,kp,ks,kc in zip(kname,koccupation,kage,kphone,kschool,kcollege):
        unclekids.objects.create(uncle=pinstance,name=kn,occupation=ko,age=ka,phone=kp,school=ks,college=kc)
    
        
def setpaternalauntdetails(id,data):
    criminalid = criminal.getcriminal(id)
    pname=data.getlist('paternalauntname')
    pocc=data.getlist('paternalauntoccupation')
    page=data.getlist('paternalauntage')
    pphone=data.getlist('paternalauntphone')
    
    for pn,po,pa,pp in zip(pname,pocc,page,pphone):
        ainstance=aunt.objects.create(criminal=criminalid,name=pn,occupation=po,age=pa,phone=pp)
    
    wname=data.getlist('paternalauntspousename')
    wage=data.getlist('paternalauntspouseage')
    wphone=data.getlist('paternalauntspousephone')
    wfather=data.getlist('paternalauntspousefather')
    waddress=data.getlist('paternalauntspouseaddress')
    woccupation=data.getlist('paternalauntspousefatheroccupation')
    
    for wn,wa,wp,wf,wad,wo in zip(wname,wage,wphone,wfather,waddress,woccupation):
        auntspouse.objects.create(aunt=ainstance,name=wn,phone=wp,age=wa,do=wf,address=wad,occupation=wo)
    
    kname=data.getlist('paternalauntkid')
    koccupation=data.getlist('paternalauntkidoccupation')
    kage=data.getlist('paternalauntkidage')
    kphone=data.getlist('paternalauntkidphone')
    kschool=data.getlist('paternalauntkidschool')
    kcollege=data.getlist('paternalauntkidcollege')
    
    for kn,ko,ka,kp,ks,kc in zip(kname,koccupation,kage,kphone,kschool,kcollege):
        auntkids.objects.create(aunt=ainstance,name=kn,occupation=ko,age=ka,phone=kp,school=ks,college=kc)        
                

def setmaternaluncledetails(id,data):
    criminalid = criminal.getcriminal(id)
    pname=data.getlist('maternalunclename')
    pocc=data.getlist('maternaluncleoccupation')
    page=data.getlist('maternaluncleage')
    pphone=data.getlist('maternalunclephone')
    
    for pn,po,pa,pp in zip(pname,pocc,page,pphone):
        minstance=maternaluncle.objects.create(criminal=criminalid,name=pn,occupation=po,age=pa,phone=pp)
    
    wname=data.getlist('maternalunclespousename')
    wage=data.getlist('maternalunclespouseage')
    wphone=data.getlist('maternalunclespousephone')
    wfather=data.getlist('maternalunclespousefather')
    waddress=data.getlist('maternalunclespouseaddress')
    woccupation=data.getlist('maternalunclespousefatheroccupation')
    
    for wn,wa,wp,wf,wad,wo in zip(wname,wage,wphone,wfather,waddress,woccupation):
        maternalunclespouse.objects.create(maternaluncle=minstance,name=wn,phone=wp,age=wa,do=wf,address=wad,occupation=wo)
    
    kname=data.getlist('maternalunclekid')
    koccupation=data.getlist('maternalunclekidoccupation')
    kage=data.getlist('maternalunclekidage')
    kphone=data.getlist('maternalunclekidphone')
    kschool=data.getlist('maternalunclekidschool')
    kcollege=data.getlist('maternalunclekidcollege')
    
    for kn,ko,ka,kp,ks,kc in zip(kname,koccupation,kage,kphone,kschool,kcollege):
        maternalunclekids.objects.create(maternaluncle=minstance,name=kn,occupation=ko,age=ka,phone=kp,school=ks,college=kc) 
        

def setmaternalauntdetails(id,data):
    criminalid = criminal.getcriminal(id)
    pname=data.getlist('maternalauntname')
    pocc=data.getlist('maternalauntoccupation')
    page=data.getlist('maternalauntage')
    pphone=data.getlist('maternalauntphone')
    
    for pn,po,pa,pp in zip(pname,pocc,page,pphone):
        minstance=maternalaunt.objects.create(criminal=criminalid,name=pn,occupation=po,age=pa,phone=pp)
    
    wname=data.getlist('maternalauntspousename')
    wage=data.getlist('maternalauntspouseage')
    wphone=data.getlist('maternalauntspousephone')
    wfather=data.getlist('maternalauntspousefather')
    waddress=data.getlist('maternalauntspouseaddress')
    woccupation=data.getlist('maternalauntspousefatheroccupation')
    
    for wn,wa,wp,wf,wad,wo in zip(wname,wage,wphone,wfather,waddress,woccupation):
        maternalauntspouse.objects.create(maternalaunt=minstance,name=wn,phone=wp,age=wa,do=wf,address=wad,occupation=wo)
    
    kname=data.getlist('maternalauntkid')
    koccupation=data.getlist('maternalauntkidoccupation')
    kage=data.getlist('maternalauntkidage')
    kphone=data.getlist('maternalauntkidphone')
    kschool=data.getlist('maternalauntkidschool')
    kcollege=data.getlist('maternalauntkidcollege')
    
    for kn,ko,ka,kp,ks,kc in zip(kname,koccupation,kage,kphone,kschool,kcollege):
        maternalauntkids.objects.create(maternalaunt=minstance,name=kn,occupation=ko,age=ka,phone=kp,school=ks,college=kc) 
  
  
        
def setmilitancydetails(id,data):
    criminalid = criminal.getcriminal(id)
    militant = data['militant']
    if militant == '1':
        militancydetails.objects.create(criminal=criminalid,organization=data['outfit'], rank=data['rank'], militancy=data['militancydetails'],
                                        infiltration=data['infiltrationdetails'], areas=data['areasofconcentration'], sympathizers=['sympathizers'],
                                        arrest=['detailsofarrest'], recoveries=data['recoveries'], associates=data['associates'])
    else:
        pass
        


def setdetentiondetails(id,data):
    criminalid = criminal.getcriminal(id)
    detentiondetails.objects.create(criminal=criminalid,history=data['detentionhistory'],detentionplace=data['place'],prision=['Prision'],date=data['detentiondate'])

def setinterrogatordetails(id,data):
    criminalid = criminal.getcriminal(id)
    interrogratoropnion.objects.create(criminal=criminalid,name=data['interrogatorname'],place=data['interrogationplace'],date=data['interrogationdate'],opnion=data['iopnion'])