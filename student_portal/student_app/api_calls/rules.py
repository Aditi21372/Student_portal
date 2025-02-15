from typing import Dict, Any, List
from .config import API_CONFIG

class Rule:
    def __init__(self, rule_id: int):
        self.rule_id = rule_id
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement check_rule")

class MandatoryCoreRule(Rule):
    def __init__(self):
        super().__init__(rule_id=0)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'coreCourses': [],
                'totalCredits': 0
            }
        }

class MandatoryBucketRule(Rule):
    def __init__(self):
        super().__init__(rule_id=1)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'studentBucketCourses': [],
                'completedBuckets': [],
                'totalCredits': 0
            }
        }

class SSHRule(Rule):
    def __init__(self):
        super().__init__(rule_id=2)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': False,
            'isCompleteText': 'Incomplete',
            'data': {
                'courses': [],
                'totalCredits': 0
            }
        }

class CWRule(Rule):
    def __init__(self):
        super().__init__(rule_id=3)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': False,
            'isCompleteText': 'Incomplete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class SGRule(Rule):
    def __init__(self):
        super().__init__(rule_id=4)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': False,
            'isCompleteText': 'Incomplete',
            'data': {
                'courses': [],
                'totalCredits': 0
            }
        }

class ThirtyTwoCreditsRule(Rule):
    def __init__(self):
        super().__init__(rule_id=5)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': False,
            'isCompleteText': 'Incomplete',
            'data': {
                'totalCredits': 0,
                'courseData': []
            }
        }

class IPRule(Rule):
    def __init__(self):
        super().__init__(rule_id=6)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Not Done',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class OnlineCoursesRule(Rule):
    def __init__(self):
        super().__init__(rule_id=7)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Not Done',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class TwoXXRule(Rule):
    def __init__(self):
        super().__init__(rule_id=8)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Not Done',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class BTPRule(Rule):
    def __init__(self):
        super().__init__(rule_id=9)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Not Done',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class IncompleteGradeRule(Rule):
    def __init__(self):
        super().__init__(rule_id=10)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'courseData': []
            }
        }

class Required156CreditsRule(Rule):
    def __init__(self):
        super().__init__(rule_id=11)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': False,
            'isCompleteText': 'Incomplete',
            'data': 0
        }

class CSAICSECoreRule(Rule):
    def __init__(self):
        super().__init__(rule_id=12)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class CSAICoreRule(Rule):
    def __init__(self):
        super().__init__(rule_id=13)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class CSAIApplicationRule(Rule):
    def __init__(self):
        super().__init__(rule_id=14)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class CSAIMathsCoreRule(Rule):
    def __init__(self):
        super().__init__(rule_id=15)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class ECOMajorCore(Rule):
    def __init__(self):
        super().__init__(rule_id=16)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class ECOMajorElective(Rule):
    def __init__(self):
        super().__init__(rule_id=17)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class SSHMajor(Rule):
    def __init__(self):
        super().__init__(rule_id=19)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class CombinesCSSSRule(Rule):
    def __init__(self):
        super().__init__(rule_id=20)
        
    def check_rule(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        # Implementation from Angular rule
        return {
            'isCompleteBool': True,
            'isCompleteText': 'Complete',
            'data': {
                'totalCredits': 0,
                'courses': []
            }
        }

class RuleManager:
    def __init__(self):
        self.rules = [
            MandatoryCoreRule(),
            MandatoryBucketRule(),
            SSHRule(),
            CWRule(),
            SGRule(),
            ThirtyTwoCreditsRule(),
            IPRule(),
            OnlineCoursesRule(),
            TwoXXRule(),
            BTPRule(),
            IncompleteGradeRule(),
            Required156CreditsRule(),
            CSAICSECoreRule(),
            CSAICoreRule(),
            CSAIApplicationRule(),
            CSAIMathsCoreRule(),
            ECOMajorCore(),
            ECOMajorElective(),
            SSHMajor(),
            CombinesCSSSRule()
        ]
        
    def get_rule(self, rule_id: int) -> Rule:
        for rule in self.rules:
            if rule.rule_id == rule_id:
                return rule
        raise ValueError(f"Rule with ID {rule_id} not found")
        
    def check_all_rules(self, student_data: Dict[str, Any], context: Any) -> Dict[str, Any]:
        results = {}
        for rule in self.rules:
            results[rule.rule_id] = rule.check_rule(student_data, context)
        return results
