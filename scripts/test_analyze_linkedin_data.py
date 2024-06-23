import unittest
from analyze_linkedin_data import analyze_linkedin_profile

class TestAnalyzeLinkedInData(unittest.TestCase):

    def test_analyze_linkedin_profile(self):
        profile_data = {
            'localizedFirstName': 'John',
            'localizedLastName': 'Doe',
            'headline': 'Software Engineer',
            'summary': 'Experienced software engineer with a passion for developing innovative programs.',
            'positions': {
                'values': [
                    {
                        'title': 'Senior Software Engineer',
                        'company': {'name': 'Tech Company'},
                        'startDate': {'year': 2018, 'month': 6},
                        'endDate': {'year': 2021, 'month': 8},
                        'summary': 'Developed and maintained software applications.'
                    }
                ]
            },
            'educations': {
                'values': [
                    {
                        'schoolName': 'University of Technology',
                        'degree': 'Bachelor of Science',
                        'fieldOfStudy': 'Computer Science',
                        'startDate': {'year': 2010, 'month': 9},
                        'endDate': {'year': 2014, 'month': 6}
                    }
                ]
            },
            'skills': {
                'values': [
                    {'skill': {'name': 'Python'}},
                    {'skill': {'name': 'Java'}}
                ]
            },
            'certifications': {
                'values': [
                    {
                        'name': 'Certified Java Developer',
                        'authority': 'Oracle',
                        'startDate': {'year': 2015, 'month': 5},
                        'endDate': {'year': 2018, 'month': 5}
                    }
                ]
            },
            'projects': {
                'values': [
                    {
                        'name': 'Project Alpha',
                        'description': 'Developed a web application for project management.',
                        'startDate': {'year': 2019, 'month': 1},
                        'endDate': {'year': 2019, 'month': 12}
                    }
                ]
            }
        }

        expected_output = {
            'name': 'John Doe',
            'headline': 'Software Engineer',
            'summary': 'Experienced software engineer with a passion for developing innovative programs.',
            'positions': [
                {
                    'title': 'Senior Software Engineer',
                    'company': 'Tech Company',
                    'start_date': {'year': 2018, 'month': 6},
                    'end_date': {'year': 2021, 'month': 8},
                    'description': 'Developed and maintained software applications.'
                }
            ],
            'education': [
                {
                    'school': 'University of Technology',
                    'degree': 'Bachelor of Science',
                    'field_of_study': 'Computer Science',
                    'start_date': {'year': 2010, 'month': 9},
                    'end_date': {'year': 2014, 'month': 6}
                }
            ],
            'skills': ['Python', 'Java'],
            'certifications': [
                {
                    'name': 'Certified Java Developer',
                    'authority': 'Oracle',
                    'start_date': {'year': 2015, 'month': 5},
                    'end_date': {'year': 2018, 'month': 5}
                }
            ],
            'projects': [
                {
                    'name': 'Project Alpha',
                    'description': 'Developed a web application for project management.',
                    'start_date': {'year': 2019, 'month': 1},
                    'end_date': {'year': 2019, 'month': 12}
                }
            ]
        }

        self.assertEqual(analyze_linkedin_profile(profile_data), expected_output)

    def test_analyze_linkedin_profile_missing_fields(self):
        profile_data = {
            'localizedFirstName': 'Jane',
            'localizedLastName': 'Smith',
            'headline': 'Data Scientist',
            'positions': {
                'values': []
            },
            'educations': {
                'values': []
            },
            'skills': {
                'values': []
            },
            'certifications': {
                'values': []
            },
            'projects': {
                'values': []
            }
        }

        expected_output = {
            'name': 'Jane Smith',
            'headline': 'Data Scientist',
            'summary': '',
            'positions': [],
            'education': [],
            'skills': [],
            'certifications': [],
            'projects': []
        }

        self.assertEqual(analyze_linkedin_profile(profile_data), expected_output)

    def test_analyze_linkedin_profile_partial_data(self):
        profile_data = {
            'localizedFirstName': 'Alice',
            'localizedLastName': 'Johnson',
            'headline': 'Product Manager',
            'summary': 'Experienced product manager with a focus on user experience.',
            'positions': {
                'values': [
                    {
                        'title': 'Product Manager',
                        'company': {'name': 'Innovative Solutions'},
                        'startDate': {'year': 2017, 'month': 3},
                        'endDate': {'year': 2020, 'month': 12},
                        'summary': 'Led product development teams.'
                    }
                ]
            },
            'educations': {
                'values': []
            },
            'skills': {
                'values': [
                    {'skill': {'name': 'Project Management'}}
                ]
            },
            'certifications': {
                'values': []
            },
            'projects': {
                'values': []
            }
        }

        expected_output = {
            'name': 'Alice Johnson',
            'headline': 'Product Manager',
            'summary': 'Experienced product manager with a focus on user experience.',
            'positions': [
                {
                    'title': 'Product Manager',
                    'company': 'Innovative Solutions',
                    'start_date': {'year': 2017, 'month': 3},
                    'end_date': {'year': 2020, 'month': 12},
                    'description': 'Led product development teams.'
                }
            ],
            'education': [],
            'skills': ['Project Management'],
            'certifications': [],
            'projects': []
        }

        self.assertEqual(analyze_linkedin_profile(profile_data), expected_output)

if __name__ == '__main__':
    unittest.main()
