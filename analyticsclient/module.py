import analyticsclient.constants.data_format as DF
from analyticsclient.exceptions import InvalidRequestError


class Module(object):
    """ Module related analytics data. """

    def __init__(self, client, course_id, module_id):
        """
        Initialize the Module client.

        Arguments:
            client (analyticsclient.client.Client): The client to use to access the API.
            course_id (str): String identifying the course
            module_id (str): String identifying the module
        """
        self.client = client
        self.course_id = unicode(course_id)
        self.module_id = unicode(module_id)

    def answer_distribution(self, data_format=DF.JSON):
        """
        Get answer distribution data for a module.

        Arguments:
            data_format (str): Format in which to return data (default is JSON)
        """
        path = 'problems/{0}/answer_distribution/'.format(self.module_id)

        return self.client.get(path, data_format=data_format)

    def submission_counts(self, module_ids, data_format=DF.JSON):
        """
        Get submission counts data for multiple modules.

        Arguments:
            module_ids (list[str]): IDs of modules for which data should be returned
            data_format (str): Format in which to return data (default is JSON)
        """
        if not module_ids:
            raise InvalidRequestError('At least one module ID must be supplied.')

        module_ids = ','.join(module_ids)
        path = 'problems/submission_counts/?problem_ids={}'.format(module_ids)

        return self.client.get(path, data_format=data_format)

    def part_ids(self, module_ids, data_format=DF.JSON):
        """
        Get part IDs for multiple modules.

        Arguments:
            module_ids (list[str]): IDs of modules for which data should be returned
            data_format (str): Format in which to return data (default is JSON)
        """
        if not module_ids:
            raise InvalidRequestError('At least one module ID must be supplied.')

        module_ids = ','.join(module_ids)
        path = 'problems/part_ids/?problem_ids={}'.format(module_ids)

        return self.client.get(path, data_format=data_format)

    def grade_distribution(self, data_format=DF.JSON):
        """
        Get grade distribution data for a module.

        Arguments:
            data_format (str): Format in which to return data (default is JSON)
        """
        path = 'problems/{0}/grade_distribution/'.format(self.module_id)

        return self.client.get(path, data_format=data_format)

    def sequential_open_distribution(self, data_format=DF.JSON):
        """
        Get open distribution data for a module.

        Arguments:
            data_format (str): Format in which to return data (default is JSON)
        """
        path = 'problems/{0}/sequential_open_distribution/'.format(self.module_id)

        return self.client.get(path, data_format=data_format)
