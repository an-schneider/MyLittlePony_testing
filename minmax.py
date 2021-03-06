
def findextremes(num_list):
    """ returns the smallest and largest elements in an inputted list
    :param: num_list
    :returns: the smallest and largest elements in input num_list
    :raises: TypeError: Input list must not be empty
    :raises: ValueError: Numbers in list must be real numbers
    :raises: ImportError: Numpy must be installed in Env
    """

    # Set up logger
    import logging
    log_format = '%(levelname)s %(asctime)s %(message)s'
    logging.basicConfig(filename='divlog.txt', format=log_format,
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,
                    filemode='w')
    logger = logging.getLogger()
    # Make sure list criteria are met
    try:
        check_input(num_list)
    except ValueError:
        logging.error('Input must be a list composed of real, numeric entries')
        quit()
    except TypeError:
        logging.error('Input must be list with entries')
        quit()
    try:
        import numpy as np
    except ImportError:
        logging.error('Numpy must be installed in your local environment!')
    logger.info("# Find Minimum and Maximum")
    logger.debug('Input: %s', str(num_list))
    minimum = np.min(num_list)
    maximum = np.max(num_list)
    logging.info("# Return Minimum and Maximum")
    logger.debug('Output:%s,%s', str(minimum),str(maximum))
    return [minimum, maximum]


def contains_imaginary(num_list):
    '''Checks if input contains imaginary numbers
    :param: num_list
    :returns: Boolean indicating if the input contains imaginary numbers
    '''
    import numpy as np
    is_real = np.isreal(num_list)
    if False in is_real:
        imaginary_elements = True
    else:
        imaginary_elements = False
    return imaginary_elements


def check_list(num_list):
    '''Checks if input is a list
    :param: num_list
    :returns: Boolean indicating if the input data type is a list'''
    if type(num_list) == list:
        list_input = True
    else:
        list_input = False
    return list_input


def check_input(num_list):
    '''Checks if the input meets all of the criteria required of minmax.py
     :param: num_list
     :raises: TypeError: If the input is not a list
     :raises: TypeError: If the input list has no entries
     :raises: ValueError: If the input list contains imaginary elements'''
    # Check that input is a list
    if check_list(num_list) is False:
        raise TypeError('Input must be a list')
    # Check that list has entries
    if len(num_list) == 0:
        raise TypeError('Input list is empty')
    # Check for imaginary numbers in list
    if contains_imaginary(num_list) is True:
        logging.error('Input list contains imaginary elements')
        raise ValueError('Input list contains imaginary elements!')
