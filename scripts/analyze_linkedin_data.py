def analyze_linkedin_profile(profile_data):
    """
    Analyzes LinkedIn profile data and formats it according to ATS or HackerRank criteria.

    Args:
        profile_data (dict): LinkedIn profile data obtained from the API.

    Returns:
        dict: Formatted resume data.
    """
    formatted_resume = {
        'name': profile_data.get('localizedFirstName', '') + ' ' + profile_data.get('localizedLastName', ''),
        'headline': profile_data.get('headline', ''),
        'summary': profile_data.get('summary', ''),
        'positions': [],
        'education': [],
        'skills': [],
        'certifications': [],
        'projects': []
    }

    # Extract positions (work experience)
    if 'positions' in profile_data:
        for position in profile_data['positions']['values']:
            formatted_resume['positions'].append({
                'title': position.get('title', ''),
                'company': position.get('company', {}).get('name', ''),
                'start_date': position.get('startDate', {}),
                'end_date': position.get('endDate', {}),
                'description': position.get('summary', '')
            })

    # Extract education
    if 'educations' in profile_data:
        for education in profile_data['educations']['values']:
            formatted_resume['education'].append({
                'school': education.get('schoolName', ''),
                'degree': education.get('degree', ''),
                'field_of_study': education.get('fieldOfStudy', ''),
                'start_date': education.get('startDate', {}),
                'end_date': education.get('endDate', {})
            })

    # Extract skills
    if 'skills' in profile_data:
        for skill in profile_data['skills']['values']:
            formatted_resume['skills'].append(skill.get('skill', {}).get('name', ''))

    # Extract certifications
    if 'certifications' in profile_data:
        for certification in profile_data['certifications']['values']:
            formatted_resume['certifications'].append({
                'name': certification.get('name', ''),
                'authority': certification.get('authority', ''),
                'start_date': certification.get('startDate', {}),
                'end_date': certification.get('endDate', {})
            })

    # Extract projects
    if 'projects' in profile_data:
        for project in profile_data['projects']['values']:
            formatted_resume['projects'].append({
                'name': project.get('name', ''),
                'description': project.get('description', ''),
                'start_date': project.get('startDate', {}),
                'end_date': project.get('endDate', {})
            })

    return formatted_resume

if __name__ == '__main__':
    import json
    profile_data = json.loads(input("Enter LinkedIn profile data in JSON format: "))
    formatted_resume = analyze_linkedin_profile(profile_data)
    print("Formatted Resume Data:")
    print(json.dumps(formatted_resume, indent=4))
