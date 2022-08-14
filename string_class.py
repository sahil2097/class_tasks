import logging
logging.basicConfig(filename='string.log', level= logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s")

class string:
    logging.info("logging into the class string")

# 1 . Try to extract data from index one to index 300 with a jump of 3
    def extract_data(self, data):
        """ extract_data is used to find the data with 3 jumps """
        self.data = data
        try:
            logging.info("trying to access string")
            s1 = data[1:300:3]
            logging.info("The required string is %s", s1)
            return s1
        except Exception as e:
            logging.exception(e)

# 2. Try to reverse a string without using reverse function
    def reverse_str(self, data):

        """ reverse_str is used to reverse the string """
        self.data = data
        try:
            logging.info("applying reverse string function")
            s1 = data[::-1]
            logging.info(" The reversed string is %s ", s1)
            return s1
        except Exception as e:
            logging.exception(e)

# 3. Try to split a string after conversion of entire string in uppercase
    def str_upper(self, data):

        """ str_upper is used to convert string to upper case """
        self.data = data
        try:
            logging.info("Applying upper case function")
            s1 = data.upper().split(" ")
            logging.info(" upper case function result is %s", s1)
            return s1
        except Exception as e:
            logging.exception(e)

# 4. try to convert the whole string into lower case
    def str_lower(self, data):

        """ str_lower is used to convert string to lower case """
        self.data = data
        try:
            logging.info(" Applying lower case function ")
            s1 = data.lower()
            logging.info(" Lower case result is %s", s1)
            return s1
        except Exception as e:
            logging.exception(e)

# 5 . Try to capitalize the whole string
    def str_capitalize(self, data):

        """ str_capitalize is used to convert string to capitalize the data """
        self.data = data
        try:
            logging.info(" Applying string capitalize function")
            s1 = data.capitalize()
            logging.info("capitalize sentence is %s", s1)
            return s1
        except Exception as e:
            logging.info(e)



s = "this is My First Python programming class and i am learNING python string and its function"
st = string()
st.str_upper(s)