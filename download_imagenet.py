import libtorrent as lt
import time
ses = lt.session()
ses.listen_on(6881, 6891)
params = {
'save_path': '/home/ai-lab/ali/torrent',
'storage_mode': lt.storage_mode_t(2),
#'paused': False,
#'auto_managed': True,
#'duplicate_is_error': True
}
#link = "magnet:?xt=urn:btih:bf62f5051ef878b9c357e6221e879629a9b4b172&tr=http%3A%2F%2Facademictorrents.com%2Fannounce.php&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969" #imagenet32x32
link = "magnet:?xt=urn:btih:96816a530ee002254d29bf7a61c0c158d3dedc3b&tr=http%3A%2F%2Facademictorrents.com%2Fannounce.php&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969"  #imagenet64x64
handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()
print ('downloading metadata...')
#while (not handle.has_metadata()):
#time.sleep(1)
    #print ('got metadata, starting torrent download...')
while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
'downloading', 'finished', 'seeding', 'allocating']
    print ('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
            s.num_peers, state_str[s.state]))
    time.sleep(10)