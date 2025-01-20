class Applicant:
    def __init__(self, name, job_title_application, soft_skills):
        self.name = name
        self.job_title_application = job_title_application
        self.soft_skills = soft_skills
        self.interviews_score = []

    def add_interview_score(self, interview_score):
        self.interviews_score.append(interview_score)

    def get_average_interview_score(self):
        if len(self.interviews_score) > 0:
            return sum(self.interviews_score)/len(self.interviews_score)
        else:
            return None
    
    def __str__(self):
        soft_skills_str = ', '.join(self.soft_skills)
        average_interview_score = self.get_average_interview_score()
        if average_interview_score is None:
                average_interview_score = "No interview scores yet"
        return f"{self.name}, {self.job_title_application}, Skills: {soft_skills_str}, Average Interview Score: {average_interview_score}"


class ML_User:
    def __init__(self, is_mathmatician, has_master_or_phd, years_experience, known_tools):
        self.is_mathmatician = is_mathmatician
        self.has_master_or_phd = has_master_or_phd
        self.years_experience = years_experience
        self.known_tools = known_tools

    def __str__(self):
        known_tools_str = ', '.join(self.known_tools)
        return f"Is Mathmatician: {self.is_mathmatician}, Has Masters or PHD: {self.has_master_or_phd}, Years of Experience: {self.years_experience}, Known Tools: {known_tools_str}"


class ML_Applicant(Applicant, ML_User):
    def __init__(self, name, job_title_application, soft_skills, is_mathmatician, has_master_or_phd, years_experience, known_tools):
        Applicant.__init__(self, name, job_title_application, soft_skills)
        ML_User.__init__(self, is_mathmatician, has_master_or_phd, years_experience, known_tools)

    def __str__(self):
        applicant_str = Applicant.__str__(self)
        ml_user_str = ML_User.__str__(self)
        return f"{applicant_str}, {ml_user_str}"
        
class ApplicantsPool:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, applicant):
        self.applicants.append(applicant)

    def __iter__(self):
        for applicant in self.applicants:
            yield applicant

if __name__ == "__main__":
    ml_applicants_pool = ApplicantsPool()
    ml_applicants_pool.add_applicant(ML_Applicant("Ricardo", "Junior ML Engineer", ["Communication", "Critical Thinking"], True, True, 8, ["Python", "R", "Java"]))
    ml_applicants_pool.add_applicant(ML_Applicant("Not chosen candidate", "Junior ML Engineer", ["Miscommunication", "Follower thinking"], False, False, 0, []))

    for applicant in ml_applicants_pool:
        if applicant.name == "Ricardo":
            applicant.add_interview_score(80)
            applicant.add_interview_score(85)
        print(applicant)

