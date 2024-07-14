import React from 'react';
import styled from '@emotion/styled';

const Crimesummary: React.FC = () => {
  return (
    <Container>
      <Header>지역별 범죄 요약 페이지</Header>
      {/* 지역별 범죄 요약 페이지의 내용 */}
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

export default Crimesummary;
