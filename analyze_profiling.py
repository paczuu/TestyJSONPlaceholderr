import pstats
from memory_profiler import profile

@profile
def analyze_memory_usage():
    # Example function to simulate memory usage
    data = [i for i in range(100000)]
    del data



def analyze_profiling_data(file_path):
    p = pstats.Stats(file_path)
    p.strip_dirs()
    p.sort_stats(pstats.SortKey.CUMULATIVE)
    p.print_stats(10)  # Print the top 10 functions

    total_time = 0
    io_bound_time = 0

    for func, (cc, nc, tt, ct, callers) in p.stats.items():
        total_time += ct
        if 'requests' in func[0] or 'urllib3' in func[0]:
            io_bound_time += ct

    cpu_bound_time = total_time - io_bound_time

    print(f"Total time: {total_time:.2f}s")
    print(f"CPU-bound time: {cpu_bound_time:.2f}s")
    print(f"IO-bound time: {io_bound_time:.2f}s")

    if cpu_bound_time > io_bound_time:
        print("The application is CPU-bound.")
    else:
        print("The application is IO-bound.")



if __name__ == '__main__':
    analyze_memory_usage()

    # Analyze each profiling file
    analyze_profiling_data('profile_posts.prof')
    analyze_profiling_data('profile_post_detail.prof')
    analyze_profiling_data('profile_albums.prof')
    analyze_profiling_data('profile_album_detail.prof')