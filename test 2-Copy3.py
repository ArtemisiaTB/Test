#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyvis.network import Network


# In[2]:


net = Network(notebook=True, cdn_resources="remote", font_color= "Black" , select_menu=True, filter_menu=True,)


# In[3]:


net.add_node(1, label="Santa Maria di Mazzarino")


# In[4]:


net.add_node(2, label="San Giorgio di Gratteri")


# In[5]:


net.add_node(3, label="Saint Mary of Pedale")


# In[6]:


net.add_node(4, label="Saint Michael the Archangel")


# In[7]:


net.add_node(5, label="Saint Peter of Sclafani")


# In[8]:


net.add_node(6, label="Saint Mary of Castronuovo")


# In[9]:


net.add_node(7, label="Saint Steven of Castronuovo")


# In[10]:


net.add_node(8, label="Santa Maria di Adriano")


# In[11]:


net.add_node(9, label="Holy Trinity of Refesio")


# In[12]:


net.add_node(10, label="Saint Nicholas of Ysa")


# In[13]:


net.add_node(11, label="Saint George of Triocala")


# In[14]:


net.add_node(12, label="Saint Mary of Jummarriis")


# In[15]:


net.add_node(13, label="Holy Cross of Buccheri")


# In[16]:


net.add_node(14, label="Saint Mary Nuova")


# In[17]:


net.add_node(15, label="Holy Spirit of Palermo")


# In[18]:


net.add_node(16, label="Holy Trinity of the Chancellor")


# In[19]:


net.add_node(17, label="Saint Mary of the Crypt")


# In[20]:


net.add_node(18, label="Saint Mary of the Chancellor or of the Latins")


# In[21]:


net.add_node(19, label="Saint Mary of the Admiral")


# In[22]:


net.add_node(20, label="Hospital of All Saints of Palermo")


# In[23]:


net.add_node(21, label="Saint Peter of Palermo")


# In[24]:


net.add_node(22, label="Saint Andrew of Bebene")


# In[25]:


net.add_node(23, label="Saint Mary of Gala")


# In[26]:


net.add_node(24, label="Saint Anne of Gala")


# In[27]:


net.add_node(25, label="Saint Philip of Saint Lucy")


# In[28]:


net.add_node(26, label="Saint Mary of Mili")


# In[29]:


net.add_node(27, label="Saint Mary of Roccamadore")


# In[30]:


net.add_node(28, label="Saint Philip the Great")


# In[31]:


net.add_node(29, label="Saint Nicholas of Paternò")


# In[32]:


net.add_node(30, label="Saint Lucy of Adernò")


# In[33]:


net.add_node(31, label="Saint Elias the Prophet")


# In[34]:


net.add_node(32, label="Saint Michael of Troina")


# In[35]:


net.add_node(33, label="Saint Mary of Maniace")


# In[36]:


net.add_node(34, label="Christ the Savior of Placa")


# In[37]:


net.add_node(35, label="Saints Peter and Paul of Agrò")


# In[38]:


net.add_node(36, label="Saint Mary of Mandanici")


# In[39]:


net.add_node(37, label="Saint Nicander of San Nicone")


# In[40]:


net.add_node(38, label="Saints Peter and Paul of Italà")


# In[41]:


net.add_node(39, label="Saint Nicholas of Pellera")


# In[42]:


net.add_node(40, label="Saint Mary delle Scale")


# In[43]:


net.add_node(41, label="Christ the Savior of Patti")


# In[44]:


net.add_node(42, label="Saint Nicholas of Fico")


# In[45]:


net.add_node(43, label="Saint Bartholomew of Lipari")


# In[46]:


net.add_node(44, label="Christ the Savior and Saints Peter and Paul of Cefalù")


# In[47]:


net.add_node(45, label="Count Roger")


# In[48]:


net.add_node(46, label="Adelasia")


# In[49]:


net.add_node(47, label="Geoffrey Secretus")


# In[50]:


net.add_node(48, label="Roger II")


# In[51]:


net.add_node(49, label="William I")


# In[52]:


net.add_node(50, label="William II")


# In[53]:


net.add_node(51, label="Judith of H")


# In[54]:


net.add_node(52, label="Walter")


# In[55]:


net.add_node(53, label="Matthew")


# In[56]:


net.add_node(54, label="George")


# In[57]:


net.add_node(55, label="Robert H")


# In[58]:


net.add_edges([(45, 2), (45, 11), (45, 25), (45, 26), (45, 27), (45, 28), (45, 32), (45, 33), (45, 34), (45, 36), (45, 37), (45, 38), (45, 40), (45, 41), (45, 42), (45, 43)])


# In[59]:


net.add_edges([(46, 3), (46, 23), (46, 24), (46, 30), (46, 31), (46, 33), (46, 39), (46, 40)])


# In[60]:


net.add_edges([(49, 8), (51, 12), (50, 14), (53, 16), (53, 18), (53, 20), (54, 19)])


# In[61]:


net.show("social_network1.html")


# In[ ]:





# In[ ]:




