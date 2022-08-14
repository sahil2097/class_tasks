import logging

logging.basicConfig(filename='list1.log', level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")


class list1:

    # Try to extract all the list entity
    def list_extract(self, data):

        """ This function is used to extract list from the data """

        logging.info("applying list extraction function")
        try:
            l = []
            for i in data:
                if type(i) == list:
                    l.append(i)
            logging.info(" the list has been extracted ")
            logging.info(l)
            return l
        except Exception as e:
            logging.info("the exception is %s", str(e))

    # Try to extract all the numerical data it may b a part of dict key and values
    def numerical_data(self, data):

        """ numerical_data function is used to filter out numerical data """

        logging.info("Applying numerical data extraction function")
        self.data = data
        try:
            a = []
            for i in data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            a.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int:
                            a.append(k)
                        if type(v) == int:
                            a.append(v)
            logging.info("numerical data extraction complete")
            logging.info(a)
            #return a
        except Exception as e:
            logging.exception(e)

    # q7 : Try to give summation of all the numeric data

    def numeric_sum(self, data):

        """ Numeric_sum function is used to find sum of all numeric data """

        logging.info("We are applying numeric sum function")
        self.data = data
        sum1 = 0
        try:
            logging.info(" Entering in try block")
            for i in data:
                if type(i) == int:
                    sum1 = sum1 + i
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            sum1 = sum1 + j
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int:
                            sum1 = sum1 + k
                        if type(v) == int:
                            sum1 = sum1 + v
            logging.info("The sum of all numeric data is {}".format(sum1))
            return sum1
        except Exception as e:
            logging.exception(e)

    def odd_number(self):

        """ odd_number function is used to find odd numbers """
        data = input(" please input data ")
        logging.info(" Applying odd number function")
        try:
            l = []
            for i in data:
                if type(i) == int:
                    if i % 2 == 0:
                        pass
                    else:
                        l.append(i)
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            if j % 2 != 0:
                                l.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int:
                            if k % 2 != 0:
                                l.append(k)
                        if type(v) == int:
                            if v % 2 != 0:
                                l.append(v)
            logging.info(" the odd numbers are {}".format(l))
            return l
        except Exception as e:
            logging.exception(e)

    # q10 :Try to find out a number of occurences of all the data

    def occurrence(self, data):

        """ occurrence function is used to find number of repetition """
        self.data = data
        logging.info(" Applying occurrence function ")
        try:
            s = []
            for i in data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        s.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        s.append(k)
                        s.append(v)
            logging.info(" The full list is {}".format(s))
        except Exception as e:
            logging.exception(e)
        try:
            logging.info(" finding occurrences ")
            # m = set(s)
            for i in set(s):
                logging.info(i, " occurred ", s.count(i), " times")
        except Exception as e:
            logging.exception(e)

    # q11 : Try to find out number of keys in dict element
    def numberofkeys(self, data):

        """ numberofkeys function is used to find number of keys element in data """
        self.data = data
        logging.info(" applying number of keys function")
        try:
            count = 0
            for i in data:
                if type(i) == dict:
                    for k in i.keys():
                        count += 1
            logging.info(" Total number of keys are {} ".format(count))
            return count
        except Exception as e:
            logging.exception(e)

    # q12 : Try to filter out all the string data
    def string_finder(self, data):

        """ string_finder function is used to find strings in the data """
        self.data = data
        logging.info(" Applying string finder function ")
        try:
            for i in data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            logging.info(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == str:
                            logging.info(k)
                        if type(v) == str:
                            logging.info(v)
        except Exception as e:
            logging.exception(e)

    # q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset
    def multiplication(self, data):

        """ multiplication function is used to find multiplication of each type of data type"""
        self.data = data
        logging.info(" Applying multiplication function")
        try:
            for i in data:
                mul = 1
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            mul = mul * j
                    logging.info(mul)
                if type(i) == dict:
                    for k in i.items():
                        for n in k:
                            if type(n) == int:
                                mul = mul * n
                    logging.info(mul)

        except Exception as e:
            logging.exception(e)
logging.shutdown()
l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
     {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
l1 = list1()
# l1.list_extract(l)
# l1.numerical_data(l)
# l1.numeric_sum(l)
#l1.odd_number(l)
l1.occurrence(l)
# l1.numberofkeys(l)
# l1.string_finder(l)
#l1.multiplication(l)
