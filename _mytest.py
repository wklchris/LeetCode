from line_profiler import LineProfiler

def timetest(func, *para):
    p = LineProfiler()
    p.add_function(func)
    p.enable_by_count()

    p_wrapper = p(func)
    p_wrapper(*para)
    
    # Printing
    print(func(*para))
    p.print_stats()
