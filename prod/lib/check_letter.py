def check_letter(candidate_letter,current_selection):

    # This function will check for redundant letters
    
    # Redundancy status is false for now
    status = False
    
    # Iterate through all currently selected letters
    
    for each in current_selection:
    
        # if the candidate letter for potential
        # selection is equal to any previously
        # selected letters, dump
        
        if candidate_letter == each:
        
            # Redundancy status changes to true
            
            status = True
    
    # Return the redundancy status        
    return status
    
if __name__ == "__main__":
	check_letter(candidate_letter,current_selection)