import os
import c4d
from c4d import gui


def main():
    """
    Use on copies!!
    export all c4d files in given directory to FBX, OBJ and C4D sub-directories. 
    Saved C4D is version of running app, eg r19 if running in r19.
       
    """
    try:
        importDpath = c4d.gui.InputDialog('Insert path of the C4D files directory', '~/Desktop/old-files')
        importpath = os.path.expanduser(importDpath)
        newfolder1 = str(importpath + '/FBX_export')
        newfolder2 = str(importpath + '/OBJ_export')
        newfolder3 = str(importpath + '/C4D_export')
        
        if not os.path.exists(newfolder1):  # check if path exist
            os.makedirs(newfolder1)
            
        if not os.path.exists(newfolder2):  # check if path exist
            os.makedirs(newfolder2)
            
        if not os.path.exists(newfolder3):  # check if path exist
            os.makedirs(newfolder3)


        files = os.listdir(importpath)
        if files:
            for afile in files:
                if afile.endswith('.c4d'):
                    print('opening file: {}'.format(afile))
                    path = os.path.join(importpath, afile)
                    c4d.documents.LoadFile(path)
                    exportpath1 = os.path.join(newfolder1, '{}.fbx'.format(afile.split('.')[0]))
                    exportpath2 = os.path.join(newfolder2, '{}.obj'.format(afile.split('.')[0]))
                    exportpath3 = os.path.join(newfolder3, '{}.c4d'.format(afile.split('.')[0]))
                    doc = c4d.documents.GetActiveDocument()
                    if c4d.documents.SaveDocument(doc, exportpath1, c4d.SAVEDOCUMENTFLAGS_0, 1026370):
                        print('file successful exported')
                    else:
                        print('error occurred writing fbx file')
                    if c4d.documents.SaveDocument(doc, exportpath2, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_OBJ2EXPORT):
                        print('file successful exported')
                    else:
                        print('error occurred writing obj file')
                    if c4d.documents.SaveDocument(doc, exportpath3, c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT):
                    	print('file successful saved')
                    else:
                        print('error occurred saving c4d file')
        else:
            gui.MessageDialog('No c4d files found in given folder!')

    finally:
        c4d.documents.CloseAllDocuments()


if __name__ == '__main__':
    main()
