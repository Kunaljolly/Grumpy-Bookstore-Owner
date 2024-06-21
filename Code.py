class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Calculate the total satisfied customers during non-grumpy minutes
        total_satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        
        # Initialize variables for the sliding window
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        
        # Slide the window over the grumpy array
        for i in range(len(grumpy)):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            if i >= minutes:
                # Remove the customer count from the window's leftmost position
                current_additional_satisfied -= customers[i - minutes] * grumpy[i - minutes]
            # Update the maximum additional satisfied customers
            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
        
        # Add the total satisfied customers and the additional satisfied customers
        return total_satisfied + max_additional_satisfied
