from .api_handler import APIHandler
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

def run_api_calls(roll_number=None) -> Dict[str, Any]:
    """Consolidated function to run all API calls with branch-specific logic"""
    api_handler = APIHandler()
    
    outputs = {
        "roll_number": roll_number,
        "student_data": {},
        "course_data": {},
        "ssh_courses": {},
        "discipline_courses": {},
        "csai_courses": {},
        "eco_major": {},
        "btp_credits": {},
        "ip_credits": {},
        "online_courses": {},
        "two_xx_courses": {}
    }
    
    try:
        # Get student data including branch
        logger.info(f"Fetching student data for roll number: {roll_number}")
        student_data = api_handler.get_student_data(roll_number)
        outputs['student_data'] = student_data
        logger.info(f"Student data received: {student_data}")
        
        # Get branch from student data
        branch = student_data.get('branch', '')
        logger.info(f"Branch identified: {branch}")
        
        # Get branch-specific data
        logger.info("Fetching course data...")
        outputs['course_data'] = api_handler.get_course_data(roll_number, branch)
        logger.info(f"Course data received: {outputs['course_data']}")
        
        logger.info("Fetching SSH courses...")
        outputs['ssh_courses'] = api_handler.get_ssh_courses(roll_number, branch)
        logger.info(f"SSH courses received: {outputs['ssh_courses']}")
        
        logger.info("Fetching discipline courses...")
        outputs['discipline_courses'] = api_handler.get_discipline_courses(roll_number, branch)
        logger.info(f"Discipline courses received: {outputs['discipline_courses']}")
        
        # CSAI specific courses
        if branch == 'CSAI':
            logger.info("Fetching CSAI courses...")
            outputs['csai_courses'] = api_handler.get_csai_courses(roll_number)
            logger.info(f"CSAI courses received: {outputs['csai_courses']}")
        
        # ECO Major courses for CSSS
        if branch == 'CSSS':
            logger.info("Fetching ECO Major core courses...")
            outputs['eco_major']['core'] = api_handler.get_eco_major_core(roll_number)
            logger.info("Fetching ECO Major elective courses...")
            outputs['eco_major']['elective'] = api_handler.get_eco_major_elective(roll_number)
            logger.info(f"ECO Major courses received: {outputs['eco_major']}")
        
        # Additional course requirements
        logger.info("Fetching BTP credits...")
        outputs['btp_credits'] = api_handler.get_btp_credits(roll_number)
        logger.info(f"BTP credits received: {outputs['btp_credits']}")
        
        logger.info("Fetching IP credits...")
        outputs['ip_credits'] = api_handler.get_ip_credits(roll_number)
        logger.info(f"IP credits received: {outputs['ip_credits']}")
        
        logger.info("Fetching online courses...")
        outputs['online_courses'] = api_handler.get_online_course_credits(roll_number)
        logger.info(f"Online courses received: {outputs['online_courses']}")
        
        logger.info("Fetching 2XX level courses...")
        outputs['two_xx_courses'] = api_handler.get_two_xx_courses(roll_number, branch)
        logger.info(f"2XX level courses received: {outputs['two_xx_courses']}")
        
    except Exception as e:
        logger.error(f"Error running API calls: {str(e)}")
        # Add error information to outputs
        outputs['error'] = str(e)
        outputs['details'] = "Failed to complete all API calls"
    
    return outputs
