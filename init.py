from multiprocessing import Manager, Process, Lock
import master_core

if __name__ == '__main__':
    with Manager() as manager:
        videos = manager.dict()
        # 'file_name' : [[keeper_ids], user_id, 'file_path', size]
        keepers = manager.dict()
        # 'keeper_node_ip' : [{'port_numbers' : is_busy}, is_alive]
        
        lv = Lock()
        lk = Lock()

        processes = []
        
        for _ in range(2):
            processes.append(Process(target=master_core.init_master_process, args=(videos, keepers, lv, lk)))
        
        for p in processes:
            p.start()
        
        for p in processes:
            p.join()
