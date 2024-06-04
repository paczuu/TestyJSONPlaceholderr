import pstats

p = pstats.Stats('profiler/profile_posts.prof')
p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(10)

p = pstats.Stats('profiler/profile_post_detail.prof')
p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(10)

p = pstats.Stats('profiler/profile_albums.prof')
p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(10)

p = pstats.Stats('profiler/profile_album_detail.prof')
p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(10)


