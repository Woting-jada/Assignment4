from utils import create_data_lists

if __name__ == '__main__':
    # create_data_lists(voc07_path='../hw4_dataset/VOCTrainVal/VOCdevkit/VOC2007',
    #                   voc12_path='../hw4_dataset/VOCTest/VOCdevkit/VOC2007',
    #                   output_folder='./')
    create_data_lists(voc07_test_path='../hw4_dataset/VOCTest/VOCdevkit/VOC2007',
                      voc07_train_path='../hw4_dataset/VOCTrainVal/VOCdevkit/VOC2007',
                      output_folder='./')