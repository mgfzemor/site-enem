import logging

logger = logging.getLogger(__name__);

def openFile(data_path,open_mode):
    data_dict = {};
    data = None;
    try:
        logger.debug("Opening file {} as {} mode.".format(data_path,open_mode));
        data = open(data_path,open_mode);
    except Exception as e:
        logger.error("Exception during open file: {}".format(e));
    return data;

def createDict(data):
    try:
        logger.debug("Creating data dictionary.")
        data_dict = {};
        columns = data.next(); # get the columns name from csv
        columns = columns.replace("\r\n",""); # remove end of line
        columns = columns.split(",");
        for index, column in enumerate(columns):
            data_dict[column] = index;
    except Exception as e:
        logger.error("Exception during create data dictionary: {}".format(e));
    return data_dict;

def readLine(data):
    try:
        logger.debug("Reading line from file");
        columns = data.next();
        columns = columns.replace("\r\n",""); # remove end of line
        columns = columns.split(",");
    except Exception as e:
        logger.error("Exception during readLine: {}".format(e));
    return columns;
