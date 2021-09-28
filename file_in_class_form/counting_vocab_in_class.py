#!/usr/bin/env python
# coding: utf-8

# In[1]:


class logger:
    def __init__(self, log_name = "log.txt"):
        self.log_name = log_name
        self.f = open(f"{self.log_name}",'w')
    
    def write_log(self,message,level='INFO'):
        self.f = open(f"{self.log_name}",'a')
        self.f.write(f"{level} :: {message}\n")
        self.f.close()
    
    
    def __del__(self):
        self.f.close()


# In[2]:


class count_vocab:
    def __init__(self , input_source = "input.txt", output_destination = "output.txt" ,log_name = "log.txt"):
        
        #Initialization
        self.temp_loger =logger(log_name)#make logger 
        self.__total_dictionary = {}#make table
        
        #read
        self.read(f"{input_source}")
        
        #process
        self.counting(self.input_readlines)
        
        #write
        y = self.write(f"{output_destination}")
        
        
    #@staticmethod
    def read(self,source):
        try:
            f = open(f"{source}",'r')
            self.input_readlines = f.readlines()
            f.close()
            self.temp_loger.write_log("source file open","INFO")
            return True
        except:
            self.temp_loger.write_log("can't open file!","ERR ")
            return False
        
        
    #@staticmethod
    def write(self,source):
        
        output = []
        for key,value in self.__total_dictionary.items():
            output.append(f'{key},{value}\n')
        print(output)
        
        try:
            f = open(f"{source}",'w')
            f.writelines(output)
            f.close()
            self.temp_loger.write_log("destination file was created","INFO")
            return True
        except:
            self.temp_loger.write_log("can't close file for writing!","ERR ")
            return False
    
    

    def preProcessing_line(self,line):
        punctuation = ['.', '?', '!', 
           ',', ';', ':', 
           '-', 'â', 'â', 
           '"', '...', '(', 
           ')', '(', ')', 
           'â', '/', '<', 
           '>', '{', '}',
           '&']
        line_without_punctuation = line
        for i in punctuation:
            line_without_punctuation = line_without_punctuation.replace(i, "")       
        
        return line_without_punctuation

    def counting(self, context_inarray_form):
        temp = []
        for line in context_inarray_form:
            temp = self.preProcessing_line(line)
            temp = temp.lower().strip().split(" ")
            for vocab in temp:
                try:
                    self.__total_dictionary[vocab] = self.__total_dictionary[vocab] + 1 
                    self.temp_loger.write_log(f"find a another {vocab} in context","INFO")
                except:
                    self.__total_dictionary[vocab] = 1     
                    self.temp_loger.write_log(f"first a first {vocab} in context","INFO")
                    


# In[3]:


x = count_vocab()


# In[4]:


n = count_vocab("input2.txt","output2.txt","log2.txt")

