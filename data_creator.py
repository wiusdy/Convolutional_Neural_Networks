from random_walk.utils.utils import Utils
import argparse

def main(args):
    utils = Utils()
    
    DATASET = args.dataset  # [MALARIA, VRD, MIT67, UNREL]

    EXTRACTOR = args.extractor

    POOLING = args.pooling

    TRAIN = 0.8

    TEST = 0.2

    kfold_split = True

    kfold_split_number = 5

    # utils.create_gcn_labels_file(DATASET=DATASET)

    RANDOM_WALK_STEP = args.walk

    # utils.show_information(DATASET=DATASET, EXTRACTOR=EXTRACTOR, TRAIN=TRAIN, TEST=TEST)
    images = utils.build_image_and_bounding_box_data(DATASET=DATASET)

    '''
    All the graphs
    '''
    fc, rw, rc, rwec, icrw, rec, fc_time, rw_time, rc_time, rwec_time, icrw_time, rec_time = utils.create_graph_data(DATASET=DATASET, EXTRACTOR=EXTRACTOR, POOLING=POOLING, images=images,
                                   RANDOM_WALK_STEP=RANDOM_WALK_STEP)

    '''
    Saving the process time
    '''

    # utils.save_process_time(DATASET=DATASET, FC_TIME=fc_time, RW_TIME=rw_time, RC_TIME=rc_time, WALK=RANDOM_WALK_STEP, MODEL=EXTRACTOR, R_CLUSTER_TIME=icrw_time, R_EDGE_TIME=rec_time, R_WEIGHTED_TIME=rwec_time)

    '''
    Creating the data for gcn
    '''
    # folds = utils.create_data(DATASET=DATASET, EXTRACTOR=EXTRACTOR, POOLING=POOLING, kfold=kfold_split, train=TRAIN, kfold_size=kfold_split_number)

    '''
    Saving data in KIPF way
    '''
    # utils.create_and_save_gcn_data(DATASET=DATASET, EXTRACTOR=EXTRACTOR, folds=folds, FC=fc, RW=rw, RC=rc, RWEC=rwec, REC=rec, ICRW=icrw, RANDOM_WALK_STEP=RANDOM_WALK_STEP)


    # utils.save_connections(graph=fc, DATASET=DATASET, EXTRACTOR=EXTRACTOR, type='')
    # utils.save_connections(graph=rw, DATASET=DATASET, EXTRACTOR=EXTRACTOR, type='Random Walk', walk=RANDOM_WALK_STEP)
    # utils.save_connections(graph=rc, DATASET=DATASET, EXTRACTOR=EXTRACTOR, type='Random Cut', walk=RANDOM_WALK_STEP)
    # utils.save_connections(graph=rec, DATASET=DATASET, EXTRACTOR=EXTRACTOR, type='Random Edge Creation', walk=RANDOM_WALK_STEP)
    # utils.save_connections(graph=rwec, DATASET=DATASET, EXTRACTOR=EXTRACTOR, type='Random Weighted Cut', walk=RANDOM_WALK_STEP)
    # utils.save_connections(graph=icrw, DATASET=DATASET, EXTRACTOR=EXTRACTOR, type='Random Cluster Cut', walk=RANDOM_WALK_STEP)


    # print('FINISHED THE CREATION OF GCN DATA FOR DATASET={} EXTRATOR={} STEP={}'.format(DATASET, EXTRACTOR, RANDOM_WALK_STEP))   

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Data processing')

    parser.add_argument('--walk', type=int, default=1,
                        help='The number of walks to give')

    parser.add_argument('--dataset', type=str, default='UNREL',
                        help='The to process')

    parser.add_argument('--extractor', type=str, default='VGG16',
                        help='The number of walks to give')

    parser.add_argument('--pooling', type=str, default='avg',
                        help='The number of walks to give')

    args = parser.parse_args()

    print(args)

    main(args)
