import React from 'react';
import { Sheet, Typography } from '@mui/joy';

interface SnapCellProps {
  title: string;
  content: string;
}

const SnapCell: React.FC<SnapCellProps> = ({ title, content }) => {
  return (
    <Sheet
      variant="outlined"
      sx={{
        p: 2,
        borderRadius: 'sm',
        boxShadow: 'md',
        backgroundColor: 'background.surface',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <Typography level="h5" textAlign="center">
        {title}
      </Typography>
      <Typography level="body2" textAlign="center">
        {content}
      </Typography>
    </Sheet>
  );
};

export default SnapCell;
