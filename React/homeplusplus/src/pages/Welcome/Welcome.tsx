import React from 'react';
import styled from '@emotion/styled';

const Welcome: React.FC = () => {
  return (
    <Container>
      <Header>웰컴 페이지</Header>
      {/* 웰컴 페이지의 내용 */}
    </Container>
  );
};

// 컨테이너 스타일
const Container = styled.div`
  padding: 20px;
`;

// 헤더 스타일
const Header = styled.h1`
  font-size: 24px;
  color: #333;
`;

export default Welcome;
