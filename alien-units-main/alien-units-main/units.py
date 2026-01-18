def convert(ratios, from_unit, to_unit, value):
    # If the units are the same, no conversion is needed
    if from_unit == to_unit:
        return value
    
    # Check if we have a direct conversion
    if (from_unit, to_unit) in ratios:
        return value / ratios[(from_unit, to_unit)]
    if (to_unit, from_unit) in ratios:
        return value * ratios[(to_unit, from_unit)]
    
    # Build a graph of conversions for easier traversal
    graph = {}
    for (unit1, unit2), ratio in ratios.items():
        if unit1 not in graph:
            graph[unit1] = {}
        if unit2 not in graph:
            graph[unit2] = {}
        
        graph[unit1][unit2] = 1 / ratio  # From unit1 to unit2
        graph[unit2][unit1] = ratio      # From unit2 to unit1
    
    # Use breadth-first search to find a conversion path
    queue = [(from_unit, value)]
    visited = {from_unit}
    
    while queue:
        current_unit, current_value = queue.pop(0)  # Dequeue from the front
        
        # Skip if the unit is not in the graph
        if current_unit not in graph:
            continue
            
        for next_unit, conversion_ratio in graph[current_unit].items():
            if next_unit == to_unit:
                # Found a direct conversion to the target unit
                return current_value * conversion_ratio
            
            if next_unit not in visited:
                # Add the next unit to the queue
                visited.add(next_unit)
                next_value = current_value * conversion_ratio
                queue.append((next_unit, next_value))
    
    return None