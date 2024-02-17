import React from 'react';
import { ThemeProvider, createTheme, Frame, Button } from '@arwes/arwes';

const App = () => {
  const theme = createTheme();

  return (
    <ThemeProvider theme={theme}>
      <Frame>
        <h1>Hello, Arwes!</h1>
        <Button>Hello</Button>
      </Frame>
    </ThemeProvider>
  );
};

export default App;
