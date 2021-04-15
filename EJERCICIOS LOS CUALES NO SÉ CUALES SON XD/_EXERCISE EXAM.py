#!/usr/bin/env python
# coding: utf-8

# # EJERCICIO

# In[56]:


## leer nombre de un estudiante, las notas de los tres parciales, el acumulado de inasistencias y 
## calcular la nota definitiva sabiendo que PP (primer parcial) tiene un % del 35% y el restante 30% es 
## para el tercer parcial. Imprimir la nota definitiva más un concepto:
# Ganó academicamente                               Fallas < a 12 y nota definitiva  >= 3
# perdió academicamente                             Fallas < a 12 y nota definitiva  < 3
# perdió por inasistencia                           Fallas > a 12 y nota definitiva no importa y se divide por la mitad
# perdió academicamente y por inasistencia          Fallas > a 12 y nota definitiva < 3


# In[66]:


# definir las variables  
nombre = ("JUANCHITO") 
nota1 = 5
nota2 = 5
nota3 = 5
a_inasistencias = 11


# In[67]:


# Proceso
notaf = (nota1*0.35)+(nota2*0.35)+(nota3*0.30)


# In[68]:


if(a_inasistencias<12 and notaf>= 3):
    print("gano academicamente nota final: ",notaf)
elif(a_inasistencias<12 and notaf < 3):
    print("perdió academicamente nota final: ",notaf)
elif(a_inasistencias>12 and notaf>= 3):
    notaf=notaf/2
    print("perdió por inasistencia nota final: ", notaf)
elif(a_inasistencias>12 and notaf < 3):
    print("perdió academicamente y por inasistencia nota final: ",notaf)


# In[ ]:


JUAN SEBASTIAN CAMACHO PERDOMO 

